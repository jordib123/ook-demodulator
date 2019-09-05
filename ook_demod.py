#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Ook Demod
# Generated: Fri Aug 16 17:55:05 2019
##################################################


from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import ook_demod_block
import osmosdr
import time
import sys
import argparse


class ook_demod(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Ook Demod")

        ##################################################
        # Command Line Arguments
        ##################################################
	parser = argparse.ArgumentParser()
		
	# Python ook_demod.py -s 1e6 -r 4e3 -f 433.92e6 -m true
	parser.add_argument("-s", "--samp_rate", default=1e6, help="Sample rate of software-defined radio")
	parser.add_argument("-r", "--symbol_rate", default=4e3, help="Symbol rate of key fob")
	parser.add_argument("-f", "--frequency", default=433.92e6, help="Listening frequency")
	parser.add_argument("-m", "--manchester", default=True, help="Manchester decoder", type=str2bool)
	parser.add_argument("-o", "--output", default=None, help="Output file")

	args = parser.parse_args()
        ##################################################
        # Variables
        ##################################################
	self.frequency = frequency = float(args.frequency)
        self.symbol_rate = symbol_rate = float(args.symbol_rate)
        self.samp_rate = samp_rate = float(args.sample_rate)
	self.manchester = manchester = args.manchester
	self.output = output = args.output

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(frequency, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.ook_demod_block = ook_demod_block.blk(symbol_rate=symbol_rate, sample_rate=samp_rate, manchester_decoding=manchester, sink_file=output)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(1e-3, 1e-3, 0)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.band_pass_filter_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate, 1, 50e3, 20e3, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.ook_demod_block, 0))
        self.connect((self.osmosdr_source_0, 0), (self.band_pass_filter_0, 0))

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, 1, 50e3, 20e3, firdes.WIN_HAMMING, 6.76))

    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')
		
		
def main(top_block_cls=ook_demod, options=None):

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
