class MessageService:
    def __init__(self, message):
        self.messages = []
        
        def add_message(self, message):
            self.messages.append(message)
            
            def get_message(self):
                return self.messages
            
            def clear_messages(self):
                self.messages = []
                
            def update_message(self,id, message):
                if id<0 or id>=len(self.messages):
                    raise ValueError("Invalid message ID")
                self.messages[id]= message
                return self.messages
            return self.messages