def construct_genesis(self):
    self.construct_block(proof_no=0, prev_hash=0)


def construct_block(self, proof_no, prev_hash):
    block = Block(
        index=len(self.chain),
        proof_no=proof_no,
        prev_hash=prev_hash,
        data=self.current_data)
    self.current_data = []

    self.chain.append(block)
    return block
