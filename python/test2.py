#!/usr/bin/env python
#
# Copyright 2004,2005,2007,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, blocks
import iio_swig as iio
from gnuradio.wxgui import stdgui2, fftsink2, slider, form, scopesink2
import wx
import iio_swig as iio

try:
    from gnuradio import analog
except ImportError:
    sys.stderr.write("Error: Program requires gr-analog.\n")
    sys.exit(1)

class  my_gui_flow_graph(stdgui2.std_top_block):

    def __init__(self, frame, panel, vbox, argv):
        stdgui2.std_top_block.__init__ (self, frame, panel, vbox, argv)

        sample_rate = 122880000
        ampl = 0.1

       # src = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 2000000, ampl)
        src = iio.fmcomms_source()
        my_fft = fftsink2.fft_sink_f(panel, title="Spectrum Analyzer", sample_rate=sample_rate, ref_level = 10, y_divs=6)
        self.connect(src, my_fft)
        vbox.Add(my_fft.win, 1, wx.EXPAND)

if __name__ == '__main__':
    app = stdgui2.stdapp(my_gui_flow_graph, "GUI GNU Radio Application")
    app.MainLoop()
