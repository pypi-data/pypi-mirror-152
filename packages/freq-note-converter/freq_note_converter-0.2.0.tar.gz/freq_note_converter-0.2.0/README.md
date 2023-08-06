## freq note converter
-- -
** recently I ran into a great package, that also supports note frequency conversion**
```
import librosa

librosa.hz_to_note(440.0)
   ['A5']
    
librosa.note_to_hz(['A3', 'A4', 'A5'])
   array([ 220.,  440.,  880.])
```
I like this librosa package, thus I will not continue with my package...  
-- - 

but if you still want to use this package, here's the documentation:
### convert frequency to note and note to frequency.
##### currently, can only input frequency and note index, and not supporting note name and octave as input
```
usage example:
    input:
        import freq_note_converter

        val = freq_note_converter.from_freq(449)
        print(val.note)
    output:
        'A'
    input:
        print(val)
    output:
                    freq : 449
              note_index : 49
                    note : A
                  octave : 4
        offset_from_note : 0.351
        --------------------------------------------------
    input:
        freq_note_converter.from_note_index(49).print_me()
    output:
                    freq : 440.0
              note_index : 49
                    note : A
                  octave : 4
        offset_from_note : 0
        --------------------------------------------------
```
