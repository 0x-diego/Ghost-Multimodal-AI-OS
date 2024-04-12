from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

class Model: 
    def __init__(self):
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", trust_remote_code=True)
        self.instructions = """"""
        
    def inference(self,prompt):
        instuctions_prompt=self.instructions + prompt
        tokens = tokenizer(instuctions_prompt, return_tensors="pt")
        generated_output = self.model.generate(**tokens, use_cache=True, max_new_tokens=1000)
        decoded_output=tokenizer.batch_decode(generated_output)[0]
        return decoded_output

