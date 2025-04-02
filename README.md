# Hi, there is [Liang's Lab](https://ins.sjtu.edu.cn/people/lhong/index.html) 👋
![Total Stars](https://img.shields.io/github/stars/ai4protein?style=social)
![Total Forks](https://img.shields.io/github/forks/ai4protein?style=social)

Research on protein-directed modification and redesign based on artificial intelligence technology. 
The research content includes but is not limited to protein structure prediction and optimization, protein-directed modification, and design.

## Recent Papers
- [Immunogenicity Prediction with Dual Attention Enables Vaccine Target Selection](https://openreview.net/forum?id=hWmwL9gizZ). *ICLR*, 2025.
- [VenusMutHub: A systematic evaluation of protein mutation effect predictors on small-scale experimental data](https://www.sciencedirect.com/science/article/pii/S2211383525001650). *Acta Pharmaceutica Sinica B*, 2025.

## 🌍 Hugging Face Model Stats
```python
from huggingface_hub import HfApi
api = HfApi()
models = api.list_models(author="ai4protein")
total_downloads = sum(m.downloads for m in models)
print(f"Total Downloads: {total_downloads}")
```
(Or check out my Hugging Face profile: [Hugging Face](https://huggingface.co/ai4protein))


