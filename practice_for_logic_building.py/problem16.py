#problem statmen:- check voting eligibility for a given age (18+).


#solution


def check_vote_eligibility(identity,age):

    if age>18:

        if identity=="yes":

            print("you are eligibile to give vote ")
        else:
            print("you have not identity so you do not gave vote")
    
    else:
        print("you are no eligibile to give vote ")