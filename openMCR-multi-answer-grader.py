#! /usr/bin/env python
import csv

non_score_fields = ['Last Name', 'First Name', 'Middle Name', 'Test Form Code', 'Student ID', 'Course ID']

def compute_grades(answer_key_file,open_mcr_result_file,output_file):
    
    #build answer key dictionary
    correct_answers_dict = {}
    scores_dict = {}
    with open(answer_key_file) as answer_key_f:
        answer_key = csv.reader(answer_key_f, delimiter=",")
        for row in answer_key:
            Qno = row[0]
            answers = row[1].split("|")
            correct_answers_dict[Qno] = answers
            scores_dict[Qno] = float(row[2])
            
    #print(correct_answers_dict)
    #evaluate student answers
    with open(open_mcr_result_file) as student_responses_file, open(output_file,"w") as output_f:
        student_responses = csv.reader(student_responses_file, delimiter=",")
        output_csv_writer = csv.writer(output_f)
        
        col_names = next(student_responses) #this determines the output csv fields
        output_csv_writer.writerow(col_names+['Total'])

        for row_num,row in enumerate(student_responses):
            try:
                to_output = []
                total = 0
                response = dict([*zip(col_names,row)])
                
                for col_name in col_names:
                    if col_name in non_score_fields:
                        #print(response[col_name])
                        to_output.append(response[col_name])

                    else:
                        student_answers = response[col_name].lstrip("[").rstrip("]").split("|")
                        #print(student_answers)
                        score_per_correct = scores_dict[col_name]/len(correct_answers_dict[col_name])
                        score = 0
                        for answer in student_answers:
                            if answer in correct_answers_dict[col_name] :
                                score += score_per_correct
                            elif answer not in correct_answers_dict[col_name] :
                                score -= score_per_correct
                        score = max(0,score) 
                        to_output.append(score)
                        total += score
                
                
                to_output.append(total)
                output_csv_writer.writerow(to_output)
            except:
                print("Something went wrong in Row # {}".format(row_num))
                continue


if __name__ == '__main__':    
    import argparse
    parser = argparse.ArgumentParser(description='Open-MCR multi answer grader')
    parser.add_argument('open_mcr_result',help='path to csv file produced by open-mcr')
    parser.add_argument('answer_key',help='path to file containing answers and score for each question')
    parser.add_argument('output_file',help='path to output file where results will be written')

    args = parser.parse_args()
    compute_grades(args.answer_key,args.open_mcr_result,args.output_file)

