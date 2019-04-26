#def average (scores):
    #ave = sum (scores)/len(scores)
    #return ave

def course_grader(test_scores):
    # Your code here
    sum_of_scores= sum(test_scores)
    for test_score in test_scores:
        if test_score < 50:
            return "fail"
    average_score = sum_of_scores / len(test_scores)
    if average_score >= 70:
        return "pass"
    return "fail"





def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"
    print(course_grader([60,80,80,70,70]))  # "pass"

if __name__ == "__main__":
    main()