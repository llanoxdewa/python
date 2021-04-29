from abc import ABC,abstractmethod

class Button(ABC):

    def __init__(self,set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass


class PushButton(Button):

    def click(self):
        print('Go to {}'.format(self.__link))
    
    @Button.link.setter
    def link(self,input):
        self.__link = input
    
    @link.getter
    def link(self):
        return self.__link
    
tombol1 = PushButton('www.google.com')
tombol1.click()
