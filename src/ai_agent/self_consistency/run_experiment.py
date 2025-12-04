import hydra
from omegaconf import DictConfig

@hydra.main(
    config_path="../../../config/self_consistency",
    config_name="config.yaml",
    version_base=None
)
def main(cfg: DictConfig):
    print(cfg)

if __name__ == "__main__":
    main()