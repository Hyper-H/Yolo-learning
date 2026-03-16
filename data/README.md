# Data Directory

Place dataset-related material here.

Recommended layout:

```text
data/
├── raw/
├── processed/
└── dataset_yaml/
```

For YOLO training, the most important file is usually a dataset YAML file that defines:

- training image path
- validation image path
- class count
- class names

