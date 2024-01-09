proffesion=sys.argv[1]
num_questions=int(sys.argv[2])

def view_question(text):
    text=text.strip()
    text=text.split(';')
    question=text[0]
    correct_answer=text[1]
    options=(f'{text[2]},{text[1]}')
    options=options.split(',')
    random.shuffle(options)
    return (question, options,correct_answer)
    
    questions=[]
    good_ans=0
    with open(rf'questions\{proffesion}.txt', mode='r') as file:
        for line in file:
            questions.append(view_question(line))

        random.shuffle(questions)
        for i in range(num_questions):
            print(questions[i][0])
            for j, answer in enumerate(questions[i][1]):
                print(f'{j+1}. {answer}')

            print("enter the correct answer")

            a=int(input())
            if questions[i][1][a-1]==questions[i][2]:
                good_ans+=1
        
        print(f'number of correct answers is {good_ans}/{num_questions}')


if __name__ == '__main__':
    main()
