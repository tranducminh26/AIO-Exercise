def evaluate_classification_model(tp, fp, fn):
    
    if type(tp) != int:
        print("tp must be int")
        return 
    if type(fp) != int:
        print("fp must be int")
        return
    if type(fn) != int:
        print("fn must be int")
        return
    if not (tp > 0 and fp > 0 and fn > 0):
        print("tp and fp and fn must be greater than zero")
        return 
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1_score is {f1_score}")
    

evaluate_classification_model(2, 3, 4)