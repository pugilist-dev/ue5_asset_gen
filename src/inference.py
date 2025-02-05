import os
from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.models.download import load_model, load_config
from shap_e.util.notebooks import create_pan_cameras, decode_latent_images, gif_widget
from shap_e.util.notebooks import decode_latent_mesh
from src.config import (
    DATA_DIR, RAW_DATA_DIR, INTERIM_DATA_DIR, PROCESSED_DATA_DIR
)

class Inference:
    def __init__(self, device):
        self.device = device
        self.xm = load_model('transmitter', device=device)
        self.model = load_model('text300M', device=device)
        self.diffusion = diffusion_from_config(load_config('diffusion'))

    def inference(self,prompt: str,
                  render_config: dict,
                   batch_size: int = 4,
                   guidance_scale: float = 15.0,
                   progress: bool = True,
                   clip_denoised: bool = True,
                   use_fp16: bool = True,
                   use_karras: bool = False,
                   karras_steps: int = 64,
                   sigma_min: float = 1e-3,
                   sigma_max: float= 160,
                   s_churn=0,
                   save_images: bool = False,
                   save_3d: bool = True,
                   ):
        latents = sample_latents(
                    batch_size=batch_size,
                    model=self.model,
                    diffusion=self.diffusion,
                    guidance_scale=guidance_scale,
                    model_kwargs=dict(texts=[prompt] * batch_size),
                    progress=progress,
                    clip_denoised=clip_denoised,
                    use_fp16=use_fp16,
                    use_karras=use_karras,
                    karras_steps=karras_steps,
                    sigma_min=sigma_min,
                    sigma_max=sigma_max,
                    s_churn=s_churn,
                    )
        if save_images:
            cameras = create_pan_cameras(render_config['size'],
                                        self.device)
            for i, latent in enumerate(latents):
                images = decode_latent_images(self.xm,
                                            latent,
                                                cameras,
                                                rendering_mode=render_config['render_mode']
                                                )

            for i, image in enumerate(images):
                image.save(PROCESSED_DATA_DIR / f'output_{i}.png')
        if save_3d:
            os.makedirs(PROCESSED_DATA_DIR / prompt / "3D", exist_ok=True)
            for i, latent in enumerate(latents):
                t = decode_latent_mesh(self.xm, latent).tri_mesh()
                with open(PROCESSED_DATA_DIR / prompt / "3D"/ f'{i}.ply', 'wb') as f:
                    t.write_ply(f)
                with open(PROCESSED_DATA_DIR / prompt / "3D"/ f'{i}.obj', 'w') as f:
                    t.write_obj(f)