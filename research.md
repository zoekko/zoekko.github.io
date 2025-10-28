---
layout: default
title: Research
---

# Research

**My current research focuses on developing statistical methods to effectively mitigate stellar contamination in transmission spectroscopy, opening the door to more accurate characterization of exoplanetary atmospheres.**

Since the launch of NASA’s James Webb Space Telescope (JWST), the field of exoplanet atmosphere characterization has made remarkable advances. Using transmission spectroscopy, astronomers are now detecting molecules, clouds, and hazes on distant worlds—uncovering vital clues to planet formation and migration.

Transmission spectroscopy is a central technique in exoplanet science. When a planet passes in front of its host star, a portion of starlight travels through the planet's atmosphere, imprinting information about atmospheric composition and structure. By analyzing the transit depths at multiple wavelengths, we can build a transmission spectrum that reveals the presence of molecules such as water vapor, methane, and carbon dioxide in exoplanet atmospheres.

However, this process is complicated by stellar contamination. Stars exhibit variability and possess surface features like spots and faculae, which can mimic or obscure the signals from exoplanet atmospheres. Traditional physical models that attempt to account for this contamination often oversimplify the physics, potentially leading to biases in atmospheric studies. There are emerging models that are faithful to the full underlying physics, but these approaches are currently too computationally expensive to be incorporated into modern atmospheric retrieval frameworks.

My current work aims to overcome these challenges by **implementing Gaussian Processes into the atmospheric retrieval pipeline.** Rather than relying solely on physical models, **I am developing a flexible, data-driven framework that can effectively model the unknown and complex stellar signals present in transmission spectra.**

Gaussian Processes are a class of flexible, non-parametric statistical models that define a distribution over possible functions fitting the data, rather than assuming a specific functional form. This allows them to capture complex, unknown patterns without imposing underlying assumptions. Because they can adapt to the structure present in the observations, Gaussian Processes are well-suited for modeling the unpredictable and complex signals introduced by stellar contamination. Their ability to robustly represent correlated noise and variability makes them powerful tools for distinguishing true atmospheric features from stellar interference in transmission spectra.

As a test case, I apply this GP-aided framework to study TOI-3235b, a giant planet orbiting a small, highly variable M dwarf. M dwarfs present both an exciting opportunity and a formidable challenge for atmospheric characterization due to their high levels of stellar contamination. **Ultimately, the goal of my current work is to push the boundaries of exoplanet atmospheric characterization by implementing novel statistical frameworks that can robustly disentangle planetary signals from stellar contamination.**

*Results coming soon.*
