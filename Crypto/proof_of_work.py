@staticmethod
def proof_of_work(last_proof):
    '''this simple algorithm identifies a number f' such that hash(ff') contain 4 leading zeroes
         f is the previous f'
         f' is the new proof
        '''
    proof_no = 0
    while BlockChain.verifying_proof(proof_no, last_proof) is False:
        proof_no += 1

    return proof_no


@staticmethod
def verifying_proof(last_proof, proof):
    #verifying the proof: does hash(last_proof, proof) contain 4 leading zeroes?

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

