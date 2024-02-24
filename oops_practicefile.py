import random


class Collage(object):
    def __init__(self,name,address,clas):
        self.name = name
        self.address = address
        self.clas= clas


    def Fees_submission(self):
        fee = random.randint(10000,20000)
        if fee:
            return f'{fee}'
        else:
            None

    def Departments(self):
        Department_list = ['RCUB','KLE',"JGCO",'SK-HUKKERI','SDVS']
        # dept = random.shuffle(Department_list)
        r_choice = random.choice(Department_list)
        if r_choice == 'RCUB':
            return f'mr:{self.name} Your alloted collage is : {r_choice} '
        elif r_choice == 'KLE':
            return f'mr:{self.name} Your alloted collage is : {r_choice} '

        elif r_choice == 'SK-HUKKERI':
            return f'mr:{self.name} Your alloted collage is : {r_choice} '

        elif r_choice == 'JGCO':
            return f'mr:{self.name} Your alloted collage is : {r_choice} '

        elif r_choice == 'SDVS':
            return f'mr:{self.name} Your alloted collage is : {r_choice} '

        else:
            raise Exception("Better luck Next Time")

    def admission_order(self):
        return {
            'name':self.name,
            'course':self.Departments(),
            'fees':self.Fees_submission(),
            'address':self.address,
            'admission-order':'Your admission order genrated successfully...'

        }

collage = Collage('Parashuram-kalakutagi','Gudas','First-year')
print(collage.admission_order())



class Bank(object):
    def __init__(self,name,adarnumber,pancardnum,deposite):
        if name and len(adarnumber) == 10 and len(pancardnum) == 10 and int(deposite) >= 5000:
            self.adhar = adarnumber
            self.name = name
            self.pancard = pancardnum
            self.deposite = deposite
            self.account_number = random.randint(100000,25800025896)


        else:
            raise Exception("Somthing went wrong please full-fill requied positions")


    def Account_deatils(self):
        return {'name':self.name,
                'adhar-number':self.adhar,
                'pancard-number':self.pancard,
                'deposite':self.deposite,
                'account-number':self.account_number}




bank = Bank('parshu','2525252525','1212121212',6522)
print(bank.Account_deatils())























