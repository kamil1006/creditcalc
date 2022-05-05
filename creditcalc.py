import argparse
import math

parser = argparse.ArgumentParser(description="This program is a loan calculator.")
parser.add_argument("-t", "--type",
                    choices=["annuity", "diff"],
                    help="type of payment")
parser.add_argument("-pa", "--payment",
                    help="monthly payment amount")
parser.add_argument("-pr", "--principal",
                    help="loan principal")
parser.add_argument("-pe", "--periods",
                    help="loan periods")
parser.add_argument("-i", "--interest",
                    help="loan interest")


args = parser.parse_args()
#print( len( vars(args) ) )
#print('-----------------------')
v = vars(args)
n_args = sum([ 1 for a in v.values( ) if a])
#print(n_args)
#print('-----------------------')
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --principal=1000000 --periods=60 --interest=10
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=diff --principal=1000000 --payment=104000
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8

#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
#   /bin/python3 /home/kamil/Pythoniki/creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8


if (args.type != 'annuity' and args.type!='diff') \
    or (args.type =='diff' and (args.payment)) \
    or not (args.interest)          \
    or n_args<4:
    #or int(args.principal)  < 0     \
    #or int(args.payment)    < 0     \
    #or int(args.periods)    < 0     \
    #or float(args.interest) < 0     \
    #    :
    print('Incorrect parameters')
else:
    #print('--------')
    #print(args)
    #print('--------')
    if args.type =='diff':
        if not(int(args.principal)>0 and int(args.periods)>0 and float(args.interest)>0):
            print('Incorrect parameters')
        else:
            #print('one')
            P = int(args.principal)
            n = int(args.periods)
            loan_interest=float(args.interest)
            i = ((loan_interest/100))/(12 * 100/100) #   interest rate
            sum_of_payments = 0
            for m in range(1,n+1):
                D = math.ceil(P/n + i * (P-((P*(m-1))/n)))
                sum_of_payments = sum_of_payments + D
                print('Month ' + str(m) + ': payment is '+str(D))
            print()
            print('Overpayment = '+ str(-P + sum_of_payments))
    elif args.type =='annuity':
        #print('annuity')
        if not args.payment:
            P = int(args.principal)
            n = int(args.periods)
            loan_interest=float(args.interest)
            if P<0 or n < 0 or loan_interest< 0.0:
                 print('Incorrect parameters')
            else:
                i = ((loan_interest/100))/(12 * 100/100) #   interest rate
                A=math.ceil(P*((i*(1+i)**n))/(((1+i)**n)-1))
                print('Your annuity payment = '+str(A)+'!')
                sum_of_payments = A*n
                if sum_of_payments-P > 0:
                    print('Overpayment = ' + str(sum_of_payments-P))     
        elif not args.principal:
            loan_interest=float(args.interest)
            A = int(args.payment)
            n = int(args.periods)
            if A<0 or n < 0 or loan_interest< 0.0:
                 print('Incorrect parameters')
            else:
                i = ((loan_interest/100))/(12 * 100/100) #   interest rate
                #P =int(round(A/((i*(1+i)**n)/(((1+i)**n)-1)),0))
                P =int((A/((i*(1+i)**n)/(((1+i)**n)-1))))
                print('Your loan principal = '+str(P)+'!')
                sum_of_payments = A*n
                if sum_of_payments-P > 0:
                    print('Overpayment = ' + str(sum_of_payments-P))     
        elif not args.periods:
            loan_interest=float(args.interest)
            A = int(args.payment)
            P = int(args.principal)
            if P<0 or A < 0 or loan_interest< 0.0:
                 print('Incorrect parameters')
            else:
                i = ((loan_interest/100))/(12 * 100/100) #   interest rate
                #print(i)
                wyliczenia = A/(A-i*P)
                #print(wyliczenia)
                n = math.ceil(math.log(wyliczenia,1+i))
                left_months = n%12
                jears = int(n/12)
                #print(n)
                message = 'It will take '
                if(n>12):
                    if (jears == 1):
                        message = message + str(jears)+' year'
                        #print('It will take '+str(jears)+' years and '+str(left_months)+' months to repay this loan!')
                    else:
                        message = message + str(jears)+' years'
                    if(left_months>1):
                        message = message + ' and '  +str(left_months)+' months'
                    elif(left_months==1):    
                        message = message + ' and '  +str(left_months)+' month'

                elif(n == 1):
                    message = message + str(n)+' month'
                else:
                    message = message + str(n)+' months'

                message = message + ' to repay this loan!'
                print(message)
                sum_of_payments = A*n
                if sum_of_payments-P > 0:
                    print('Overpayment = ' + str(sum_of_payments-P))    
