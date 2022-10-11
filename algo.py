from copy import deepcopy
from time import sleep
from getshit import *

# ============================================================ #

PRINTING = True
SLEEPING = True

# MODIFIER VECTOR_SPACE EN ACCORD AVEC L'ORDRE ET LE CONTENU DE VOS QUESTIONS : 
VECTOR_SPACE = [
    [0, 1, 2, 3],   # discrete, example QCM à 4 choix
    (0, 30),   # discrete
    (0, 30),   # discrete
    (0, 30),   # discrete
    [0, 1, 2, 3],   # discrete
    (0, 30),   # discrete
    (0, 30),   # discrete
    [0, 1, 2, 3],   # discrete
    (0, 30),   # discrete
    [0, 1, 2, 3],   # discrete
    (0, 30),   # discrete
    [0, 1, 2, 3],   # discrete
    [0, 1, 2, 3],   # discrete
    [0, 1, 2, 3],   # discrete
    [0, 1, 2, 3],   # discrete
    (0, 30),   # discrete
    [0, 1, 2, 3],   # discrete
    [0, 1, 2, 3],   # discrete
    (0, 30),# continuous, example valeur entre 0 et 28 inclus (entiers)  
    (0, 30)
]
# ============================================================ #






def function_to_optimize(v):
    return sum([int(i == v[i]) for i in range(len(v))])
        

def create_random_vector(vector_space): # create a random vector
    return [3, 0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 1, 3, 2, 2, 0, 2, 1, 0, 0]
    res = []
    for space in vector_space:
            res.append(space[0])
    return res

def modify_component_vector(new_vector, component):
    if component >= len(VECTOR_SPACE):
        print("All questions have been answered")
        return new_vector
    #new_vector = deepcopy(new_vector)
    if isinstance(VECTOR_SPACE[component], list):
        next_index = VECTOR_SPACE[component].index(new_vector[component]) + 1
        if next_index >= len(VECTOR_SPACE[component]):
            return False
        new_vector[component] = VECTOR_SPACE[component][next_index]
    elif isinstance(VECTOR_SPACE[component], tuple):
        if new_vector[component] > VECTOR_SPACE[component][1]:
            return False
        new_vector[component] += 1
    return True


best_score = - float('inf')
best_vector = create_random_vector(VECTOR_SPACE)
vector_candidate = create_random_vector(VECTOR_SPACE)
question = 0


def get_next_answers(last_vector_candidate, last_last_score_candidate, last_score_candidate, question):
    
    if last_score_candidate > last_last_score_candidate:
        question_solved = True
        modify_component_vector(last_vector_candidate, question + 1)

    else:
        question_solved = False
        
        modified = modify_component_vector(last_vector_candidate, question)
        if not modified:
            question_solved = True
        
    return last_vector_candidate, question_solved



# def sendresponses(answers):
#     real = [2, 0, 0, 0, 0, 0, 0, 3]
#     score = 0
#     for i in range(len(real)):
#         if real[i] == answers[i]:
#             score += 1
#     return score

if __name__ == "__main__":
    last_vector_candidate = create_random_vector(VECTOR_SPACE)
    attempt = start(sesskey)
    sendresponses([i+1 for i in range(20)], answerid, last_vector_candidate, attempt, sesskey)
    submit(attempt, sesskey)
    last_score_candidate = getscore(sesskey) 
    last_last_score_candidate = last_score_candidate

    print("Question", question)
    print("Last vector candidate:", last_vector_candidate)
    print(f"Note: {last_score_candidate}/20")
    print()
    
    question = 0
    
    while question < len(VECTOR_SPACE):
        last_last_vector_candidate = deepcopy(last_vector_candidate)

        last_vector_candidate, question_solved = get_next_answers(last_vector_candidate, last_last_score_candidate, last_score_candidate, question)
        if question_solved:
            question += 1

        last_last_score_candidate = last_score_candidate

        attempt, answerid = start(sesskey)
        print("Sending:", last_vector_candidate)
        sendresponses([i+1 for i in range(20)], answerid, last_vector_candidate, attempt, sesskey)
        submit(attempt, sesskey)
        last_score_candidate = getscore(sesskey) 

        # print("Debugging:", last_score_candidate, last_last_score_candidate)

        if last_score_candidate < last_last_score_candidate:
            question += 1
            last_vector_candidate = last_last_vector_candidate
            last_score_candidate = last_last_score_candidate

        print("Question", question)
        print("Last vector candidate:", last_vector_candidate)
        print()



