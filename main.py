def load_transition_table(file_path):
    try: 
        with open(file_path, 'r') as f:
            lines = f.readlines()

        print("File Content:\n", lines) #debug
        
        #Parse the alphabet from the first line
        alphabet = lines[0].strip().split()
        print("Alphabet:", alphabet) #debug

        #initialize data structures
        transitions = {}
        start_state = None
        final_states = set()

        #Parse each state's transitions
        for line in lines[1:]:
            if not line.strip():
                continue

            print("Parsing line: ", line.strip())#debug
            parts = line.strip().split()
            print("split parts: ", parts)#debug

            state = int(parts[0]) #first element is the state number
            print("Mapping transitions for state:", state)  # Debugging

            if len (parts[1:1 + len(alphabet)]) != len(alphabet):
                raise ValueError(f"invlaiid number of transitions for state {state}")
            
            transitions[state] = dict(zip(alphabet, map(int, parts[1:1+len(alphabet)])))
            print(f"Parsed state {state}: {transitions[state]}")  # Debugging

            #check for 'S' and 'F' in the last part of the line
            if len(parts) > len(alphabet) + 1 and 'S' in parts[-1]:
                start_state = state
            if len(parts) > len(alphabet) + 1 and 'F' in parts[-1]:
                final_states.add(state)
        
        return alphabet, transitions, start_state, final_states
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise

def load_input_string(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()
    
def process_string(transitions, start_state, final_states, input_string):
    current_state = start_state

    for char in input_string:
        if char not in transitions[current_state]:
            print(f"error invlid charcter'{char}' for state {current_state}")
            return "No"
        if transitions[current_state][char] is None:
            print(f"error: no transition for state {current_state} on {char}")
        
        current_state = transitions[current_state][char]
    
    return "YES" if current_state in final_states else "NO"

if __name__ == "__main__":
    try:
        alphabet, transitions, start_state, final_states = load_transition_table('transition_table_sample.txt')
        print("Alphabet:", alphabet)
        print("Transitions:", transitions)
        print("Start State:", start_state)
        print("Final States:", final_states)

        #load input string
        input_string = load_input_string('sample_string.txt')
        print("Input String:", input_string)

        #process the input string
        result = process_string(transitions, start_state, final_states, input_string)
        print("Result:", result)
    
    except Exception as e:
        print("Error:", e)

    with open('transition_table_sample.txt', 'r') as f:
        print("transition table file content: \n", f.read())
    
    with open('sample_string.txt', 'r') as f:
        print("input string file content:\n", f.read())