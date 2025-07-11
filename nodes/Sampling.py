import comfy.samplers
import comfy.sample
from comfy.k_diffusion import sampling as k_diffusion_sampling
import torch

class Noise_RandomNoise:
    def __init__(self, seed):
        self.seed = seed

    def generate_noise(self, input_latent):
        latent_image = input_latent["samples"]
        batch_inds = input_latent["batch_index"] if "batch_index" in input_latent else None
        return comfy.sample.prepare_noise(latent_image, self.seed, batch_inds)
    
class MC_RandomNoise():
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {"forceInput": True}),  # Input name is "seed"
            }
        }

    RETURN_TYPES = ("NOISE",)
    FUNCTION = "get_noise"
    CATEGORY = "ComfyMC/Sampling"

    def get_noise(self, seed):  # Accepts `seed` (matches INPUT_TYPES)
        return (Noise_RandomNoise(seed),)  # Passes `seed` to Noise_RandomNoise