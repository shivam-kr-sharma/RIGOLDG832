import pyvisa
import time

class RigolDG832:
    """
    Rigol DG832 Waveform Generator
    
    This class provides functions to control and configure the Rigol DG832 waveform generator using PyVISA.
    Make sure to install the PyVISA library before using this class.

    Arguments asked in this class:

            devicename: Name of the device as listed in pyvisa.ResourceManager.open_resource() list.
            channel: Integer value(either 1 or 2 )
            state:   Either "ON" or "OFF".
            amplitude: value for the voltage, either integer or float in Vpp.
            offset: Either integer or float, in volts.
    """
    
    def __init__(self, devicename):
        """Initialize the waveform generator object with the specified device name"""
        self.devicename = devicename
        self.rm = pyvisa.ResourceManager()
        self.com = self.rm.open_resource(self.devicename)
        time.sleep(0.5)

    
    def close(self):
        """Close the connection to the waveform generator"""
        print("The device has been closed.\n")
        self.com.close()
        time.sleep(0.5)


    
    def set_channel_state(self, channel, state):
        """Set the output state of the specified channel (1 or 2)"""
        print(f" Channel {channel} has been turned {state}.\n")
        self.com.write(f"OUTPut{channel} {state}")
        time.sleep(0.5)
    
    def get_channel_state(self, channel):
        """Get the output state of the specified channel (1 or 2)"""
        print(f"The amplitude for the channel {channel} is {self.com.query(f'SOURce{channel}:VOLTAGE:AMPLITUDE?')} Vpp\n")
        print(f'Output of channel {channel} is {self.com.query(f"OUTPut{channel}:STATe?")}\n')
        time.sleep(0.5)

    def set_channel_amplitude(self, channel, amplitude):
        """Set the amplitude of the specified channel (1 or 2). Whatever value you will give, it will take that as Vpp or voltage peak to peak."""
        print(f"The amplitude of the channel {channel} has been set to {amplitude} Vpp.\n")
        self.com.write(f"SOURce{channel}:VOLTAGE:AMPLITUDE {amplitude}")
        time.sleep(0.5)
    
    def get_channel_amplitude(self, channel):
        """Get the amplitude of the specified channel (1 or 2)"""
        time.sleep(0.5)
        return print(f"The amplitude for the channel {channel} is {self.com.query(f'SOURce{channel}:VOLTAGE:AMPLITUDE?')} Vpp. \n")
        
    

    def set_channel_freq(self, channel, frequency):
        """Set the amplitude of the specified channel (1 or 2). Whatever value you will give, it will take that as Vpp or voltage peak to peak."""
        print(f"The frequency of the channel {channel} has been set to {frequency} Vpp.\n")
        self.com.write(f"SOURce{channel}:FREQuency {frequency}")
        
    
    def get_channel_freq(self, channel):
        """Get the amplitude of the specified channel (1 or 2)"""
        time.sleep(0.5)
        return print(f"The frequency for channel {channel} is {self.com.query(f'SOURce{channel}:FREQuency?')} Hz. \n")
    
    def set_channel_offset(self, channel, offset):
        """Set the offset of the specified channel (1 or 2)"""
        print(f"Channel {channel} has been set to {offset} Vdc offset value. \n")
        self.com.write(f"SOURce{channel}:VOLTAGE:OFFSET {offset}")
        time.sleep(0.5)




    
    def get_channel_offset(self, channel):
        """Get the offset of the specified channel (1 or 2)"""
        print(f"Offset value for channel {channel} is {self.com.query(f'SOURce{channel}:VOLTAGE:OFFSET?')} Volts (Vdc). \n")    
        time.sleep(0.5)


    # COUNTER Commands
    class counter:
        """
        This class is specially for counter commands.
        
        """
        def __init__(self, com):
            self.com = com

        def set_counter_state(self, state):
            """Enable or disable the frequency counter"""
            self.com.write(f"COUNTER:STATE {state}")
        
        def get_counter_state(self):
            """Get the state of the frequency counter"""
            return self.com.query("COUNTER:STATE?")
        
        def set_counter_coupling(self, coupling):
            """Set the frequency counter coupling mode"""
            self.com.write(f"COUNTER:COUPLING {coupling}")
        
        def get_counter_coupling(self):
            """Get the frequency counter coupling mode"""
            return self.com.query("COUNTER:COUPLING?")
        
        def set_counter_gate_time(self, gate_time):
            """Set the frequency counter gate time"""
            self.com.write(f"COUNTER:GATEtime {gate_time}")
        
        def get_counter_gate_time(self):
            """Get the frequency counter gate time"""
            return self.com.query("COUNTER:GATEtime?")
        
        def set_counter_high_frequency(self, high_frequency):
            """Set the high frequency limit of the frequency counter"""
            self.com.write(f"COUNTER:HF {high_frequency}")
        
        def get_counter_high_frequency(self):
            """Get the high frequency limit of the frequency counter"""
            return self.com.query("COUNTER:HF?")
        
        def set_counter_level(self, level):
            """Set the trigger level for the frequency counter"""
            self.com.write(f"COUNTER:LEVEL {level}")
        
        def get_counter_level(self):
            """Get the trigger level for the frequency counter"""
            return self.com.query("COUNTER:LEVEL?")
        
        def measure_counter(self):
            """Perform a frequency measurement using the frequency counter"""
            return self.com.query("COUNTER:MEASURE?")
        
        def set_counter_sensitivity(self, sensitivity):
            """Set the sensitivity of the frequency counter"""
            self.com.write(f"COUNTER:SENSITIVE {sensitivity}")
        
        def get_counter_sensitivity(self):
            """Get the sensitivity of the frequency counter"""
            return self.com.query("COUNTER:SENSITIVE?")
        
        def set_counter_state(self, state):
            """Enable or disable the frequency counter"""
            self.com.write(f"COUNTER:STATE {state}")
        
        def get_counter_state(self):
            """Get the state of the frequency counter"""
            return self.com.query("COUNTER:STATE?")
        
        def clear_counter_statistics(self):
            """Clear the statistics of the frequency counter"""
            self.com.write("COUNTER:STATISTICS:CLEAR")
        
        def set_counter_statistics_state(self, state):
            """Enable or disable the statistics of the frequency counter"""
            self.com.write(f"COUNTER:STATISTICS:STATE {state}")
        
        def get_counter_statistics_state(self):
            """Get the state of the statistics of the frequency counter"""
            return self.com.query("COUNTER:STATISTICS:STATE?")
    
    
    # COUPLING Commands
    class coupling:
        """
        This class is specially for coupling commands.
        
        """
        def __init__(self, com):
            self.com = com

        def set_amplitude_coupling_deviation(self, channel, deviation):
            """Set the amplitude coupling deviation for the specified channel (1 or 2)"""
            self.com.write(f"COUPLING:AMPLitude:DEViation {channel}, {deviation}")
        
        def get_amplitude_coupling_deviation(self, channel):
            """Get the amplitude coupling deviation for the specified channel (1 or 2)"""
            return self.com.query(f"COUPLING:AMPLitude:DEViation? {channel}")
        
        def set_amplitude_coupling_state(self, channel, state):
            """Enable or disable the amplitude coupling for the specified channel (1 or 2)"""
            self.com.write(f"COUPLING:AMPLitude:STATe {channel}, {state}")
        
        def get_amplitude_coupling_state(self, channel):
            """Get the state of the amplitude coupling for the specified channel (1 or 2)"""
            return self.com.query(f"COUPLING:AMPLitude:STATe? {channel}")
        
        def set_phase_coupling_state(self, state):
            """Enable or disable the phase coupling"""
            self.com.write(f"COUPLING:PHASesource:STATe {state}")
        
        def get_phase_coupling_state(self):
            """Get the state of the phase coupling"""
            return self.com.query("COUPLING:PHASesource:STATe?")
        
    # FREQUENCY Commands
    class frequency:


        """
        This class is specially for frequency commands. Also simple functionality related to frequency(like modifying frequency of different channels) is already defined above.
        
        ### An example for how one should use a class inside a class in another file after importing the first class.
        ###     from RIGOLDG832 import RigolDG832          (RIGOLDG832 is the name of the python file in which all the classes are defined.)
        ###     device = RigolDG832('USB0::0x1AB1::0x0643::DG8A220800213::INSTR')
        ###     device.frequency(device.com).set_frequency(1,4)
        
        
        """
        def __init__(self, com):
            self.com = com

            
        def set_frequency(self, channel, frequency):
            """Set the frequency of the output signal for the specified channel"""
            return self.com.write(f"SOURce{channel}:FREQuency {frequency}")

        def get_frequency(self, channel):
            """Get the frequency of the output signal for the specified channel"""
            print(f"The frequency of channel {channel} is {self.com.query(f'SOURce{channel}:FREQuency?')}")

        def set_frequency_deviation(self, channel, deviation):
            """Set the frequency deviation for the specified channel"""
            self.com.write(f"SOURce{channel}:FREQuency:DEViation {deviation}")

        def get_frequency_deviation(self, channel):
            """Get the frequency deviation for the specified channel"""
            return self.com.query(f"SOURce{channel}:FREQuency:DEViation?")

        def set_frequency_resolution(self, channel, resolution):
            """Set the frequency resolution for the specified channel"""
            self.com.write(f"SOURce{channel}:FREQuency:RESolution {resolution}")

        def get_frequency_resolution(self, channel):
            """Get the frequency resolution for the specified channel"""
            return self.com.query(f"SOURce{channel}:FREQuency:RESolution?")

        def set_frequency_sweep(self, channel, start, stop, time):
            """Configure and start the frequency sweep for the specified channel"""
            self.com.write(f"SOURce{channel}:FREQuency:STARt {start}")
            self.com.write(f"SOURce{channel}:FREQuency:STOP {stop}")
            self.com.write(f"SOURce{channel}:FREQuency:SWEep:TIME {time}")
            self.com.write(f"SOURce{channel}:FREQuency:SWEep:STATe ON")

        def get_frequency_sweep_state(self, channel):
            """Get the state of the frequency sweep for the specified channel"""
            return self.com.query(f"SOURce{channel}:FREQuency:SWEep:STATe?")

        def set_frequency_sweep_time(self, channel, time):
            """Set the time for the frequency sweep for the specified channel"""
            self.com.write(f"SOURce{channel}:FREQuency:SWEep:TIME {time}")

        def get_frequency_sweep_time(self, channel):
            """Get the time for the frequency sweep for the specified channel"""
            return self.com.query(f"SOURce{channel}:FREQuency:SWEep:TIME?")

        def set_frequency_sweep_start(self, channel, start):
            """Set the start frequency for the frequency sweep for the specified channel"""
            self.com.write(f"SOURce{channel}:FREQuency:SWEep:STARt {start}")

        def get_frequency_sweep_start(self, channel):
            """Get the start frequency for the frequency sweep for the specified channel"""
            return self.com.query(f"SOURce{channel}:FREQuency:SWEep:STARt?")

        def set_frequency_sweep_stop(self, channel, stop):
            """Set the stop frequency for the frequency sweep for the specified channel"""
            self.com.write(f"SOURce{channel}:FREQuency:SWEep:STOP {stop}")

        def get_frequency_sweep_stop(self, channel):
            """Get the stop frequency for the frequency sweep for the specified channel"""
            return self.com.query(f"SOURce{channel}:FREQuency:SWEep:STOP?")

        def set_frequency_sweep_mode(self, channel, mode):
            """Set the mode for the frequency sweep (LINear or LOGarithmic) for the specified channel"""
            self.com.write(f"SOURce{channel}:FREQuency:SWEep:MODE {mode}")

        def get_frequency_sweep_mode(self, channel):
            """Get the mode for the frequency sweep for the specified channel"""
            return self.com.query(f"SOURce{channel}:FREQuency:SWEep:MODE?")


    

    # PHASE Commands
    
    def set_phase(self, channel, phase):
        """Set the phase of the output signal for the specified channel"""
        self.com.write(f"SOURce{channel}:PHASe {phase}")
        print(f'The phase of channel { channel} is set to {self.com.query(f"SOURce{channel}:PHASe?")} degrees.\n ')
        time.sleep(0.5)

    def get_phase(self, channel):
        """Get the phase of the output signal for the specified channel"""
        time.sleep(0.5)
        print(f'Phase of channel {channel} is {self.com.query(f"SOURce{channel}:PHASesource?")} degrees. \n')
        return self.com.query(f"SOURce{channel}:PHASesource?")
        

    def set_phase_sync_state(self, channel, state):
        """Enable or disable phase synchronization for the specified channel"""
        self.com.write(f"SOURce{channel}:PHASesource:SYNC {state}")
        time.sleep(0.5)

    def get_phase_sync_state(self, channel):
        """Get the state of phase synchronization for the specified channel"""
        time.sleep(0.5)
        return self.com.query(f"SOURce{channel}:PHASesource:SYNC?")
    
    # PULSE Commands

    def set_pulse_width(self, channel, width):
        """Set the pulse width of the output signal for the specified channel"""
        self.com.write(f"SOURce{channel}:PULSe:WIDTH {width}")

    def get_pulse_width(self, channel):
        """Get the pulse width of the output signal for the specified channel"""
        print(f'Pulse width for channel {channel} is {self.com.query(f"SOURce{channel}:PULSe:WIDTH?")}')
        return self.com.query(f"SOURce{channel}:PULSe:WIDTH?")

    def set_pulse_period(self, channel, period):
        """Set the pulse period of the output signal for the specified channel"""
        self.com.write(f"SOURce{channel}:PULSe:PERiod {period}")

    def get_pulse_period(self, channel):
        """Get the pulse period of the output signal for the specified channel"""
        return self.com.query(f"SOURce{channel}:PULSe:PERiod?")

    def set_pulse_delay(self, channel, delay):
        """Set the delay between the trigger and the start of the pulse for the specified channel"""
        self.com.write(f"SOURce{channel}:PULSe:DELay {delay}")

    def get_pulse_delay(self, channel):
        """Get the delay between the trigger and the start of the pulse for the specified channel"""
        return self.com.query(f"SOURce{channel}:PULSe:DELay?")

    def set_pulse_width_modulation_state(self, channel, state):
        """Enable or disable pulse width modulation for the specified channel"""
        self.com.write(f"SOURce{channel}:PULSe:WMODulation {state}")

    def get_pulse_width_modulation_state(self, channel):
        """Get the state of pulse width modulation for the specified channel"""
        return self.com.query(f"SOURce{channel}:PULSe:WMODulation?")

    def set_pulse_width_modulation_mode(self, channel, mode):
        """Set the mode for pulse width modulation (INTernal or EXTernal) for the specified channel"""
        self.com.write(f"SOURce{channel}:PULSe:WMODulation:MODE {mode}")

    def get_pulse_width_modulation_mode(self, channel):
        """Get the mode for pulse width modulation for the specified channel"""
        return self.com.query(f"SOURce{channel}:PULSe:WMODulation:MODE?")

    def set_pulse_width_modulation_frequency(self, channel, frequency):
        """Set the frequency for pulse width modulation for the specified channel"""
        self.com.write(f"SOURce{channel}:PULSe:WMODulation:FREQuency {frequency}")

    def get_pulse_width_modulation_frequency(self, channel):
        """Get the frequency for pulse width modulation for the specified channel"""
        return self.com.query(f"SOURce{channel}:PULSe:WMODulation:FREQuency?")

    def set_pulse_width_modulation_depth(self, channel, depth):
        """Set the depth for pulse width modulation for the specified channel"""
        self.com.write(f"SOURce{channel}:PULSe:WMODulation:DEPTh {depth}")

    def get_pulse_width_modulation_depth(self, channel):
        """Get the depth for pulse width modulation for the specified channel"""
        return self.com.query(f"SOURce{channel}:PULSe:WMODulation:DEPTh?")

    # TRIGGER Commands

    class trigger:

        def __init__(self,com):
            self.com = com

        def set_trigger_source(self, source):
            """Set the trigger source (INTernal or EXTernal)"""
            self.com.write(f"TRIGger:SOURce {source}")
        
        def get_trigger_source(self):
            """Get the trigger source"""
            return self.com.query("TRIGger:SOURce?")
        
        def set_trigger_delay(self, delay):
            """Set the delay for the trigger"""
            self.com.write(f"TRIGger:DELay {delay}")
        
        def get_trigger_delay(self):
            """Get the delay for the trigger"""
            return self.com.query("TRIGger:DELay?")
        
        def set_trigger_slope(self, slope):
            """Set the trigger slope (POSitive or NEGative)"""
            self.com.write(f"TRIGger:SLOPe {slope}")
        
        def get_trigger_slope(self):
            """Get the trigger slope"""
            return self.com.query("TRIGger:SLOPe?")
        
        def set_trigger_level(self, level):
            """Set the trigger level"""
            self.com.write(f"TRIGger:LEVel {level}")
        
        def get_trigger_level(self):
            """Get the trigger level"""
            return self.com.query("TRIGger:LEVel?")
        
    # UTILITY Commands
    
    def reset_instrument(self):
        """Reset the instrument to default settings"""
        self.com.write("*RST")
    
    def clear_errors(self):
        """Clear any existing errors"""
        self.com.write("*CLS")
    
    def get_error(self):
        """Get the last error message"""
        return self.com.query("SYSTem:ERRor?")
