class NucleotideSequence:
    '''A general nucleotide class. The class is inherited by DNASequence
    and RNASequence classes. Not for general use. Use DNASequence and
    RNASequence instead'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'T',
                   'T': 'A'}
    
    def __init__(self, sequence):
        '''Input sequence should be a string,
        in all upper case letters.'''
        assert isinstance(sequence, str)
        assert len(sequence) > 0
        self.sequence = sequence
        self.base_counts = {}
    
    def base_count(self, base):
        '''Given a base, returns the number of
        times the base occurs in this sequence.
        
        Returns an integer.
        '''
        assert isinstance(base, str)
        assert len(base) == 1
        assert base == base.upper()
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count
    
    def gc_content(self):
        '''returns the proportion of residues 
        that are either G or C in the sequence,
        from 0 to 1'''
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)
        
    def reverse_complement(self):
        ''''Given a sequence returns a reverse complement of the sequence given'''
        rev_c = ""
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
        return rev_c

class DNASequence(NucleotideSequence):
    '''Class appropriate for DNA sequences. Assumes only A,T,C and G are found in the sequence.'''
    def __init__(self, sequence):
        NucleotideSequence.__init__(self, sequence)
        allowed_chars = ("A", "T", "C", "G")
        for char in set(sequence):
            assert char in allowed_chars

class RNASequence(NucleotideSequence):
    '''Class appropriate for RNA sequences. Assumes only A,U,C and G are found in the sequence.'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'U',
                   'U': 'A'}
    def __init__(self, sequence):
        NucleotideSequence.__init__(self, sequence)
        allowed_chars = ("A", "U", "C", "G")
        for char in set(sequence):
            assert char in allowed_chars

x = DNASequence('AGGCT')
y = RNASequence('AGGCU')

assert x.base_count('G') == 2
assert x.gc_content() == 0.6
assert x.reverse_complement() == 'AGCCT'
assert y.reverse_complement() == 'AGCCU'


