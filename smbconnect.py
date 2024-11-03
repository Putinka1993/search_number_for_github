import os
#from smb.SMBConnection import SMBConnection
# from app import Window_login_pass

class SMBConnect:

    def __init__(self, login, passw):
        self.userID = login#'asp-lva'
        self.password = passw#'Firsovgey33!'
        self.client_machine_name = 'ivc'

        self.server_name = '/Консист'
        self.server_ip = '10.3.6.200'
        self.domain_name = 'ln.rosenergoatom.ru'

        self.share = 'Консист'
        self.from_path = '/ОСОС/ТелДанные/'
        self.into_path = '/home/asp1-taa@ln.rosenergoatom.ru/Загрузки/ANTON/PYTHON/first_project/data/'

    #def connect(self):
            #self.conn = SMBConnection(self.userID, self.password, self.client_machine_name, self.server_name, domain=self.domain_name, use_ntlm_v2=True, is_direct_tcp=True)
            #return self.conn.connect(self.server_ip, 445)


    def download(self):
        files = self.conn.listPath(self.share, self.from_path)
        for name in files:
            if name.filename.endswith(".xlsx"): 
                with open(f'{self.into_path}{name.filename}', 'wb') as fp:
                    self.conn.retrieveFile(self.share, self.from_path + name.filename, fp)

        self.conn.close()


    
