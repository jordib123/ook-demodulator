# ook-demodulator
A GNU Radio real-time on-off keying demodulator using software-defined radio

Real-time automated on-off keying demodulator that can be used to demodulate on-off keying modulated signals. This implementation is used to demodulate signals transmitted by vehicle key fobs. Also consists of an automated Manchester decoder.

# Execution

The demodulator requires GNU Radio (https://www.gnuradio.org/) and the gr-osmosdr package (https://osmocom.org/projects/gr-osmosdr/wiki) to control the software-defined radio. Demodulator can be executed via the terminal using Python. There are 4 required parameters:

| Parameter | Default | Description |
| ------------- | ------------- | ------------- |
| -s --sample_rate | 1e6 | Sample rate of the software-defined radio.
| -r --symbol_rate | 4e3 | Symbol rate of the key fob signal. Varies for each different key fob.
| -s --frequency | 433.92e6 | Listening frequency of the software-defined radio.
| -m --manchester | True | Enable/disable manchester decoder.
| -o --output | None | If none provided the output is printed to the terminal (optional).
  
Example: _Python ook_demod.py -s 1e6 -r 4e3 -f 433.92e6 -m true_
