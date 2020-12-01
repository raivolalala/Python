@staticmethod
def check_validity(block, prev_block):
    if prev_block.index + 1 != block.index:
        return False

    elif prev_block.calculate_hash != block.prev_hash:
        return False

    elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
        return False

    elif block.timestamp <= prev_block.timestamp:
        return False

    return True
