#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Antenna Sweep module
# Author: Hans Erik Fjeld
# Description: For antenna measurement analysis
# Generated: Sat Nov 23 00:22:51 2019
##################################################


from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import limesdr


class limesdr_loopback(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Antenna Sweep module")

        ##################################################
        # Variables
        ##################################################
        self.trans_width = trans_width = 500e3
        self.samp_rate = samp_rate = 32e6
        self.sweep_tone = sweep_tone = 0
        self.step_size = step_size = samp_rate/2 - trans_width
        self.input_scale = input_scale = 1e-5
        self.gain_tx = gain_tx = int(10)
        self.gain_rx = gain_rx = int(10)
        self.freq = freq = 50e6

        ##################################################
        # Blocks
        ##################################################
        self.zmq_tx_pub = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://127.0.0.1:5000', 100, False, -1)
        self.zmq_rx_pub = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://127.0.0.1:5001', 100, False, -1)
        self.scale_tx = blocks.multiply_vcc(1)
        self.lo_input = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq + sweep_tone, 1, 0)
        self.limesdr_tx = limesdr.sink('', 0, '', '')
        self.limesdr_tx.set_sample_rate(samp_rate)
        self.limesdr_tx.set_center_freq(freq, 0)
        self.limesdr_tx.set_bandwidth(step_size,0)
        self.limesdr_tx.set_digital_filter(step_size,0)
        self.limesdr_tx.set_gain(gain_rx,0)
        self.limesdr_tx.set_antenna(255,0)
        self.limesdr_tx.calibrate(step_size, 0)

        self.limesdr_rx = limesdr.source('', 0, '')
        self.limesdr_rx.set_sample_rate(samp_rate)
        self.limesdr_rx.set_center_freq(freq, 0)
        self.limesdr_rx.set_bandwidth(step_size,0)
        self.limesdr_rx.set_digital_filter(step_size,0)
        self.limesdr_rx.set_gain(30,0)
        self.limesdr_rx.set_antenna(255,0)
        self.limesdr_rx.calibrate(step_size, 0)

        self.input_scale_source = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, input_scale)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.input_scale_source, 0), (self.scale_tx, 0))
        self.connect((self.limesdr_rx, 0), (self.zmq_rx_pub, 0))
        self.connect((self.lo_input, 0), (self.limesdr_tx, 0))
        self.connect((self.lo_input, 0), (self.scale_tx, 1))
        self.connect((self.scale_tx, 0), (self.zmq_tx_pub, 0))

    def get_trans_width(self):
        return self.trans_width

    def set_trans_width(self, trans_width):
        self.trans_width = trans_width
        self.set_step_size(self.samp_rate/2 - self.trans_width)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_step_size(self.samp_rate/2 - self.trans_width)
        self.lo_input.set_sampling_freq(self.samp_rate)

    def get_sweep_tone(self):
        return self.sweep_tone

    def set_sweep_tone(self, sweep_tone):
        self.sweep_tone = sweep_tone
        self.lo_input.set_frequency(self.freq + self.sweep_tone)

    def get_step_size(self):
        return self.step_size

    def set_step_size(self, step_size):
        self.step_size = step_size
        self.limesdr_tx.set_bandwidth(self.step_size,0)
        self.limesdr_tx.set_digital_filter(self.step_size,0)
        self.limesdr_rx.set_bandwidth(self.step_size,0)
        self.limesdr_rx.set_digital_filter(self.step_size,0)

    def get_input_scale(self):
        return self.input_scale

    def set_input_scale(self, input_scale):
        self.input_scale = input_scale
        self.input_scale_source.set_offset(self.input_scale)

    def get_gain_tx(self):
        return self.gain_tx

    def set_gain_tx(self, gain_tx):
        self.gain_tx = gain_tx

    def get_gain_rx(self):
        return self.gain_rx

    def set_gain_rx(self, gain_rx):
        self.gain_rx = gain_rx
        self.limesdr_tx.set_gain(self.gain_rx,0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.lo_input.set_frequency(self.freq + self.sweep_tone)
        self.limesdr_tx.set_center_freq(self.freq, 0)
        self.limesdr_rx.set_center_freq(self.freq, 0)


def main(top_block_cls=limesdr_loopback, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
