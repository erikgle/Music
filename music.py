import copy 

class MusicScale():

    base_scale = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    scale_order = ['w','w','h','w','w','w','h']
    
    
    def __init__(self, start = 'C', mode = 'major'):
        
        self.start = start
        self.mode = mode
        #the mode doesn't add any functionality right now, but I plan to
        #add some after the final if I continue working on this code
        
        self.starting_index = self.base_scale.index(start)
        

        
        
    def find_scale(self):
        
        """ Finds a scale based on a given starting note 
        
        Returns
        -------
        scale : list 
            A list of notes in a scale starting on the given starting note
        
        """ 
        
        scale = []
        scale.append(self.start)
        scale_index = self.starting_index
        
        for step in self.scale_order:
            if step == 'w':
                scale_index += 2
            elif step == 'h':
                scale_index += 1
                
            scale_index = scale_index % len(self.base_scale)
            #bc code won't run if the index is larger than what the length of scale order is 
            
            scale.append(self.base_scale[scale_index])
        return scale
    
    
    def find_chord(self, root):
        """ Finds a chord based on a given starting note in a particular scale
    
        Parameters
        ----------
        root : int or str
            specifies the root of the chord you would like in a given key(the key is defined based on the MusicScale object already created
            valid int inputs are 1-7, valid str inputs are any note in the scale
        
        Returns
        -------
        output  : list
            A chord (list of notes in a particular order)
        """ 
        
        output = []
        scale = self.find_scale()
        scale = scale[ : len(scale) - 1]
        #you have to do this or else the code doesn't 'wrap' correctly since the tonic gets repeated
        
        #this code makes it so that the function can take either a string or an int to specify the starting note
        
        if type(root) == str:
            
            if root in scale:
                output.append(root)
                rootindex = scale.index(root)
            else:
                return 'note not in scale'
            
        else:
            rootindex = root - 1
            output.append(scale[rootindex])
            
        third_index = (rootindex + 2) % len(scale)
        
        output.append(scale[third_index])
        
        fifth_index = (rootindex + 4) % len(scale)
        
        output.append(scale[fifth_index])
        
        return output
        
        
    def chord_progression(self, notelist):
        
        """ Allows you to input a chord progression as a list of numbers and see what it would be in a particular key
    
        Parameters
        ----------
        notelist : list of ints or str
            specifies the chords in a particular key you want to play 
            valid int inputs are 1-7, valid str inputs are any note in the scale, for each item in the list
        
        Returns
        -------
        output  : dictionary
            A dictionary in which the input chords are the keys, and the values are chords
        
        """ 
        
        prog_dictionary = {}
    
        for each in notelist:
            chord = self.find_chord(each)
            prog_dictionary[each] = chord
    
        return prog_dictionary
    
    
    def identify_chord_possibilities(self, notelist):
        
        ''' A super helpful function for chord identification, returns possible chords based on note combinations
        
        Parameters
        ----------
        notelist : list of str
            specifies which note or notes you're looking to be played in a chord simultaniously 
            
            
        Returns
        -------
        chord_output  : dictionary
            A dictionary which shows the possible chords from combinations of these notes 
        
        '''
        chord_possibilites = self.chord_progression([1,2,3,4,5,6,7])
        chord_output = self.chord_progression([1,2,3,4,5,6,7])
        #may seem redundant but if you make output = possibilities the code errors bc 
        #mutable objects update with eachother
        
        #iteration errors because the dictionary size changes as the code loops 
        
        for note in notelist:
            for each in chord_possibilites:
                if (note not in chord_possibilites[each]):
                    if each in chord_output.keys():
                    #have to check if the key even exists in this dict anymore,
                    #otherwise you get a key error because it tries to delete what's not there
                        del chord_output[each]
        
        return chord_output

#functions:


def notes_in(notelist):
        
    
    """ Searches every key in order to determine which scales have the notes inputted
    
        Parameters
        ----------
        notelist : list of str
            specifies which notes you are searching for 
        
        Returns
        -------
        output_list  : list
            A list of scales which contain all the notes you specified. May be empty if no scales contain
            all of the notes that were provided
        
        """ 
    
    init = MusicScale()
    all_possible = []
    output_list = copy.deepcopy(all_possible)
    #similar logic as before, mutable objects get confusing to work with
    #when you use them in loops
    
    for every_note in init.base_scale:
        scale = MusicScale(every_note)
        all_possible.append(scale.find_scale())
    
    output_list = copy.deepcopy(all_possible)
        
    
    for every_note in notelist:
        for every_scale in all_possible:
            #print(every_note, str(every_scale))
            #print(every_note in every_scale)
            if every_note not in every_scale and every_scale in output_list:
                
                
                output_list.remove(every_scale)
               
    
    return output_list
        