import streamlit as st
import random
from collections import Counter
import time
import os
import sys

if 'start' not in st.session_state:
    st.session_state.start = False

def bold(type): 
    sys.stdout.write("\033[1m" + type + "\033[0m")

def random_gen(nivel=0):
    if nivel == 0:
        return random.randint(1, 3)
    if nivel == 1:
        return random.randint(1, 7)
    if nivel == 2:
        return random.randint(1, 10)

def get_solutions():
    outcomes, outcomes_v2 = possible_outcomes(hexagon)

    target, possibilidades = define_the_most_common(outcomes)

    combinations = define_the_combinations(target, outcomes_v2)

    st.write("\t\t\t"*3, "Target: ", target, "  Possible solutions: ", possibilidades)
    return combinations

hexagon = [random_gen(nivel=2) for x in range(1, 20)]

def print_dict(d):
    print(d)
    # for k, v in d.items():
    #     print(k, v)

def straighline_v2(hexagon):
    possible_straigh_combinations = [[0, 3],
                                     [3, 6],
                                     [4, 7],
                                     [7, 10],
                                     [8, 11],
                                     [9, 12],
                                     [12, 15],
                                     [13, 16],
                                     [16, 19]]

    possible_straigh_combinations_letters = [["A", "B", "C"],
                                             ["D", "E", "F"],
                                             ["E", "F", "G"],
                                             ["H", "I", "J"],
                                             ["I", "J", "K"],
                                             ["J", "K", "L"],
                                             ["M", "N", "O"],
                                             ["N", "O", "P"],
                                             ["Q", "R", "S"]]

    # previously: [16, 17, 18, 20...]
    # now: {16: [A, B, C]}
    # return {sum(hexagon[possible_straigh_combinations[x][0]: possible_straigh_combinations[x][1]]) : i 
    #             for x, i in enumerate(possible_straigh_combinations_letters)}
    s2 = [{sum(hexagon[possible_straigh_combinations[x][0]: possible_straigh_combinations[x][1]]) : i}
                for x, i in enumerate(possible_straigh_combinations_letters)]
    # print_dict(s2)
    return [sum(hexagon[x[0]: x[1]]) for x in possible_straigh_combinations], s2

def straighline(hexagon):
    possible_straigh_combinations = [[0, 3],
                                     [3, 6],
                                     [4, 7],
                                     [7, 10],
                                     [8, 11],
                                     [9, 12],
                                     [12, 15],
                                     [13, 16],
                                     [16, 19]]
    
    return [sum(hexagon[x[0]: x[1]]) for x in possible_straigh_combinations]

def diagonal_v2(hexagon):
    possibles_diagonal_combinations = [[0, 3, 7],
                                       [1, 4, 8],
                                       [2, 5, 9],
                                       [4, 8, 12],
                                       [5, 9, 13],
                                       [6, 10, 14],
                                       [9, 13, 16],
                                       [10, 14, 17],
                                       [11, 15, 18],
                                       
                                       #
                                       [0,4,9],
                                       [1,5,10],
                                       [2,6,11],
                                       [3,8,13],
                                       [4,9,14],
                                       [5,10,15],
                                       [7,12,16],
                                       [8,13,17],
                                       [9,14,18]]

    possibles_diagonal_combinations_letters = [["A", "D", "H"],
                                       ["B", "E", "I"],
                                       ["C", "F", "J"],
                                       ["E", "I", "M"],
                                       ["F", "J", "N"],
                                       ["G", "K", "O"],
                                       ["J", "N", "Q"],
                                       ["K", "O", "R"],
                                       ["L", "P", "S"],
                                       #
                                       ["A","E","J"],
                                       ["B","F","K"],
                                       ["C","G","L"],
                                       ["D","I","N"],
                                       ["E","J","O"],
                                       ["F","K","P"],
                                       ["H","M","Q"],
                                       ["I","N","R"],
                                       ["J","O","S"]]
    
    # previously: [16, 18, ....]
    # now :
    d2 = [{hexagon[possibles_diagonal_combinations[x][0]] + hexagon[possibles_diagonal_combinations[x][1]] + hexagon[possibles_diagonal_combinations[x][2]] : i}
                for x, i in enumerate(possibles_diagonal_combinations_letters)]
    # print_dict(d2)
    # return {hexagon[x[0]] + hexagon[x[1]] + hexagon[x[2]] : i 
    #             for x, i in enumerate(possibles_diagonal_combinations_letters)}
    return [hexagon[x[0]] + hexagon[x[1]] + hexagon[x[2]] for x in possibles_diagonal_combinations], d2

def diagonal(hexagon):
    possibles_diagonal_combinations = [[0, 3, 7],
                                       [1, 4, 8],
                                       [2, 5, 9],
                                       [4, 8, 12],
                                       [5, 9, 13],
                                       [6, 10, 14],
                                       [9, 13, 16],
                                       [10, 14, 17],
                                       [11, 15, 18],
                                       
                                       #
                                       [0,4,9],
                                       [1,5,10],
                                       [2,6,11],
                                       [3,8,13],
                                       [4,9,14],
                                       [5,10,15],
                                       [7,12,16],
                                       [8,13,17],
                                       [9,14,18]]
    
    return [hexagon[x[0]] + hexagon[x[1]] + hexagon[x[2]] for x in possibles_diagonal_combinations]

def define_the_combinations(target, outcomes_v2):
    combinations = []
    for x in outcomes_v2:
        if target in x:
            combinations.append(x[target])

    return combinations

def define_the_most_common(all_sum):
    occurence_count = Counter(all_sum)
    # print(occurence_count)
    return occurence_count.most_common(1)[0][0], occurence_count.most_common(1)[0][1]

def possible_outcomes(hexagon):
    # print("Straights")
    straighs, s_v2 = straighline_v2(hexagon)
    # print(straighs)

    # print("Diagonals")
    diagonals, d_v2 = diagonal_v2(hexagon)
    # print(diagonals)

    all_sum_v2 = s_v2 + d_v2

    all_sum = straighs + diagonals

    return all_sum, all_sum_v2

def print_solutions(solutions):
    for s in solutions:
        c1, c2, c3 = st.columns(3)
        with c1:
            s[0]
        with c2:
            s[1]
        with c3:
            s[2]

def run():
    # First we show the hexagon
    os.system("clear")
    print_hexagon(hexagon)
    time.sleep(90) # 90

    # Second we hide everything
    os.system("clear")
    solutions = get_solutions()

    # Third time we show everything
    time.sleep(120) # 120
    solutions = print_empty()
    print_hexagon(hexagon)
    time.sleep(120) # 120

    # Fourth thing is to show the solution
    print_solutions(solutions)

def print_empty():
    A, B, C = 'A', 'B', 'C'
    D, E, F, G = 'D', 'E', 'F', 'G'
    H, I, J, K, L = 'H', 'I', 'J', 'K', 'L'
    M,N,O,P = 'M', 'N', 'O', 'P'
    Q, R, S = 'Q', 'R', 'S'

    # Define the HTML and CSS for the hexagon layout
    hexagon_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            .hexagon {{
                position: relative;
                width: 100px;
                height: 55px;
                background-color: #4CAF50; /* Hexagon background color */
                margin: 27.5px 0;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                font-size: 20px;
                font-weight: bold;
                color: white; /* Text color */
                border-radius: 5px;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Optional shadow for better visibility */
            }}

            .hexagon:before, .hexagon:after {{
                content: "";
                position: absolute;
                width: 0;
                border-left: 50px solid transparent;
                border-right: 50px solid transparent;
            }}

            .hexagon:before {{
                bottom: 100%;
                border-bottom: 27.5px solid #4CAF50; /* Same as hexagon background color */
            }}

            .hexagon:after {{
                top: 100%;
                border-top: 27.5px solid #4CAF50; /* Same as hexagon background color */
            }}

            .hexagon-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
            }}

            .hexagon-row {{
                display: flex;
                justify-content: center;
            }}
        </style>
    </head>
    <body>
        <div class="hexagon-container">
            <div class="hexagon-row">
                <div class="hexagon">{A}</div>
                <div class="hexagon">{B}</div>
                <div class="hexagon">{C}</div>
            </div>
            <div class="hexagon-row">
                <div class="hexagon">{D}</div>
                <div class="hexagon">{E}</div>
                <div class="hexagon">{F}</div>
                <div class="hexagon">{G}</div>
            </div>
            <div class="hexagon-row">
                <div class="hexagon">{H}</div>
                <div class="hexagon">{I}</div>
                <div class="hexagon">{J}</div>
                <div class="hexagon">{K}</div>
                <div class="hexagon">{L}</div>
            </div>
            <div class="hexagon-row">
                <div class="hexagon">{M}</div>
                <div class="hexagon">{N}</div>
                <div class="hexagon">{O}</div>
                <div class="hexagon">{P}</div>
            </div>
            <div class="hexagon-row">
                <div class="hexagon">{Q}</div>
                <div class="hexagon">{R}</div>
                <div class="hexagon">{S}</div>
            </div>
        </div>
    </body>
    </html>
    """

    # Streamlit app
    st.markdown(hexagon_html, unsafe_allow_html=True)

def print_hexagon(hexagon, with_solution=False):
    A, B, C = hexagon[:3]
    D, E, F, G = hexagon[3:7]
    H, I, J, K, L = hexagon[7:12]
    M,N,O,P = hexagon[12:16]
    Q, R, S = hexagon[16:19]

    if not with_solution:
        # Define the HTML and CSS for the hexagon layout - #4CAF50
        hexagon_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                .hexagon {{
                    position: relative;
                    width: 100px;
                    height: 55px;
                    background-color: red; /* Hexagon background color */
                    margin: 27.5px 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    font-size: 40px;
                    font-weight: bold;
                    color: black; /* Text color */
                    border-radius: 5px;
                    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Optional shadow for better visibility */
                }}

                .hexagon:before, .hexagon:after {{
                    content: "";
                    position: absolute;
                    width: 0;
                    border-left: 50px solid transparent;
                    border-right: 50px solid transparent;
                }}

                .hexagon:before {{
                    bottom: 100%;
                    border-bottom: 27.5px solid red; /* Same as hexagon background color */ --
                }}

                .hexagon:after {{
                    top: 100%;
                    border-top: 27.5px solid red; /* Same as hexagon background color */
                }}

                .hexagon-container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }}

                .hexagon-row {{
                    display: flex;
                    justify-content: center;
                }}
            </style>
        </head>
        <body>
            <div class="hexagon-container">
                <div class="hexagon-row">
                    <div class="hexagon">{A}</div>
                    <div class="hexagon">{B}</div>
                    <div class="hexagon">{C}</div>
                </div>
                <div class="hexagon-row">
                    <div class="hexagon">{D}</div>
                    <div class="hexagon">{E}</div>
                    <div class="hexagon">{F}</div>
                    <div class="hexagon">{G}</div>
                </div>
                <div class="hexagon-row">
                    <div class="hexagon">{H}</div>
                    <div class="hexagon">{I}</div>
                    <div class="hexagon">{J}</div>
                    <div class="hexagon">{K}</div>
                    <div class="hexagon">{L}</div>
                </div>
                <div class="hexagon-row">
                    <div class="hexagon">{M}</div>
                    <div class="hexagon">{N}</div>
                    <div class="hexagon">{O}</div>
                    <div class="hexagon">{P}</div>
                </div>
                <div class="hexagon-row">
                    <div class="hexagon">{Q}</div>
                    <div class="hexagon">{R}</div>
                    <div class="hexagon">{S}</div>
                </div>
            </div>
        </body>
        </html>
        """
    else:
        # Define the HTML and CSS for the hexagon layout
        hexagon_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                .hexagon {{
                    position: relative;
                    width: 100px;
                    height: 55px;
                    background-color: #4CAF50; /* Hexagon background color */
                    margin: 27.5px 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    font-size: 20px;
                    font-weight: bold;
                    color: white; /* Text color */
                    border-radius: 5px;
                    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Optional shadow for better visibility */
                }}

                .hexagon:before, .hexagon:after {{
                    content: "";
                    position: absolute;
                    width: 0;
                    border-left: 50px solid transparent;
                    border-right: 50px solid transparent;
                }}

                .hexagon:before {{
                    bottom: 100%;
                    border-bottom: 27.5px solid #4CAF50; /* Same as hexagon background color */
                }}

                .hexagon:after {{
                    top: 100%;
                    border-top: 27.5px solid #4CAF50; /* Same as hexagon background color */
                }}

                .hexagon-container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }}

                .hexagon-row {{
                    display: flex;
                    justify-content: center;
                }}
            </style>
        </head>
        <body>
            <div class="hexagon-container">
                <div class="hexagon-row">
                    <div class="hexagon">A={A}</div>
                    <div class="hexagon">B={B}</div>
                    <div class="hexagon">C={C}</div>
                </div>
                <div class="hexagon-row">
                    <div class="hexagon">D={D}</div>
                    <div class="hexagon">E={E}</div>
                    <div class="hexagon">F={F}</div>
                    <div class="hexagon">G={G}</div>
                </div>
                <div class="hexagon-row">
                    <div class="hexagon">H={H}</div>
                    <div class="hexagon">I={I}</div>
                    <div class="hexagon">J={J}</div>
                    <div class="hexagon">K={K}</div>
                    <div class="hexagon">L={L}</div>
                </div>
                <div class="hexagon-row">
                    <div class="hexagon">M={M}</div>
                    <div class="hexagon">N={N}</div>
                    <div class="hexagon">O={O}</div>
                    <div class="hexagon">P={P}</div>
                </div>
                <div class="hexagon-row">
                    <div class="hexagon">Q={Q}</div>
                    <div class="hexagon">R={R}</div>
                    <div class="hexagon">S={S}</div>
                </div>
            </div>
        </body>
        </html>
        """

    # Streamlit app
    st.markdown(hexagon_html, unsafe_allow_html=True)

def wait_for_time(total_time):
    start_time = time.time()

    progress_text = "You have {} seconds to look."
    my_bar = st.progress(0, text=progress_text.format(total_time))

    # Update the progress bar
    while True:
        elapsed_time = time.time() - start_time
        percent_complete = min(int((elapsed_time / total_time) * 100), 100)
        
        # Update the progress bar with the percentage complete
        my_bar.progress(percent_complete, text=progress_text.format(int(total_time - elapsed_time)))
        
        # Break the loop when the time is up
        if elapsed_time >= total_time:
            break
        
        # Sleep for a short period to avoid excessive CPU usage
        time.sleep(0.1)

st.markdown("""
    <style>
    .Start {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;  /* Center vertically */
    }
    .Start button {
        font-size: 24px; /* Make the button text larger */
        padding: 20px 40px; /* Adjust padding to make the button larger */
        border-radius: 10px; /* Optional: rounded corners */
        border: none; /* Optional: remove border */
        background-color: #4CAF50; /* Button color */
        color: white; /* Text color */
        cursor: pointer; /* Pointer cursor on hover */
    }
    </style>
""", unsafe_allow_html=True)

# Create a div container for the button with custom styling
# st.markdown('<div class="big-button"><button onclick="window.location.reload();">Start</button></div>', unsafe_allow_html=True)

# Handle the button click in Python
# if st.button("Start"):
if st.session_state.start == False:
    # Show the starting hexagon and wait 90 seconds
    print_hexagon(hexagon)
    wait_for_time(90)

    st.session_state.start = True
    st.rerun()
else:
    solutions = get_solutions()
    print_empty()
    wait_for_time(120)

with st.expander("Solutions:"):
    # Fourth thing is to show the solution
    print_solutions(solutions)
    print_hexagon(hexagon, with_solution=True)
    st.divider()
