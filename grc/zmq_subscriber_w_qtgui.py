#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: GUI for connecting with Limesdr instance
# Author: Hans Erik Fjeld
# Description: Connect to a an instance running a non GUI RF frontend
# Generated: Sat Nov 23 20:07:05 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class zmq_subscriber_w_qtgui(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "GUI for connecting with Limesdr instance")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("GUI for connecting with Limesdr instance")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "zmq_subscriber_w_qtgui")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 16e6
        self.data_len = data_len = 4096

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Frequency')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Time')
        self.top_layout.addWidget(self.tab)
        self.zmq_tx_sub = zeromq.sub_source(gr.sizeof_gr_complex, 1, 'tcp://127.0.0.1:5000', 100, True, -1)
        self.zmq_qt_rx_subscriber = zeromq.sub_source(gr.sizeof_gr_complex, 1, 'tcp://127.0.0.1:5001', 100, True, -1)
        self.qtgui_scope_sink = qtgui.time_sink_c(
        	data_len, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_scope_sink.set_update_time(0.10)
        self.qtgui_scope_sink.set_y_axis(-1, 1)

        self.qtgui_scope_sink.set_y_label('Amplitude', "")

        self.qtgui_scope_sink.enable_tags(-1, True)
        self.qtgui_scope_sink.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_scope_sink.enable_autoscale(False)
        self.qtgui_scope_sink.enable_grid(False)
        self.qtgui_scope_sink.enable_axis_labels(True)
        self.qtgui_scope_sink.enable_control_panel(True)
        self.qtgui_scope_sink.enable_stem_plot(False)

        if not True:
          self.qtgui_scope_sink.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(4):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_scope_sink.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_scope_sink.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_scope_sink.set_line_label(i, labels[i])
            self.qtgui_scope_sink.set_line_width(i, widths[i])
            self.qtgui_scope_sink.set_line_color(i, colors[i])
            self.qtgui_scope_sink.set_line_style(i, styles[i])
            self.qtgui_scope_sink.set_line_marker(i, markers[i])
            self.qtgui_scope_sink.set_line_alpha(i, alphas[i])

        self._qtgui_scope_sink_win = sip.wrapinstance(self.qtgui_scope_sink.pyqwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_scope_sink_win)
        self.qtgui_freq_sink = qtgui.freq_sink_c(
        	data_len, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink.set_update_time(0.10)
        self.qtgui_freq_sink.set_y_axis(-140, 10)
        self.qtgui_freq_sink.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink.enable_autoscale(False)
        self.qtgui_freq_sink.enable_grid(False)
        self.qtgui_freq_sink.set_fft_average(1.0)
        self.qtgui_freq_sink.enable_axis_labels(True)
        self.qtgui_freq_sink.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink.set_line_label(i, labels[i])
            self.qtgui_freq_sink.set_line_width(i, widths[i])
            self.qtgui_freq_sink.set_line_color(i, colors[i])
            self.qtgui_freq_sink.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_win = sip.wrapinstance(self.qtgui_freq_sink.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_freq_sink_win)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_scope_sink, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_freq_sink, 1))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_scope_sink, 1))
        self.connect((self.zmq_qt_rx_subscriber, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.zmq_tx_sub, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "zmq_subscriber_w_qtgui")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_scope_sink.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_data_len(self):
        return self.data_len

    def set_data_len(self, data_len):
        self.data_len = data_len


def main(top_block_cls=zmq_subscriber_w_qtgui, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
