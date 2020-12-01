def new_data(self, sender, recipient, quantity):
    self.current_data.append({
        'sender': sender,
        'recipient': recipient,
        'quantity': quantity
    })
    return True

