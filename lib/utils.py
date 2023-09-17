import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("ayoubkirouane/Stable-Cats-Generator", torch_dtype=torch.float16)
pipe = pipe.to("cuda")


def run(prompt , save_name , seed_num=None , manual_seed=False , num_inference_steps=15 ,height=512, width=512 ) : 
    image = pipe(prompt=prompt , num_inference_steps=num_inference_steps , height=height, width=width).images[0] 
    if manual_seed : 
        generator = torch.Generator("cuda").manual_seed(seed_num)
        image = pipe(prompt=prompt ,generator=generator ,  num_inference_steps=num_inference_steps , height=height, width=width).images[0]
    image.save(f"results/{save_name}.png")