class Checker:
    def check_page(self,answer):
        if answer==True:
            return True
        else:
            return answer
    def check_result(self,result):
        if type(result)==None:
            return False
        else:
            return result.text