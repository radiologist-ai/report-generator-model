# Тестовый отчет
## подготовка
- скачать датасет IU по [ссылке](https://drive.google.com/file/d/1uLIbyM01jvJURcRmclUsLvLd9vJAmwCG/view?usp=sharing)
- распаковать в папку data
- активировать виртуальное окружение 
- - `python -venv venv`
- - `.\venv\Scripts\activate`
- установить зависимости 
- - `python -m pip install poetry`
- - `python -m poetry install --no-root`
- запустить проект (версий несколько, я пробовал 12 и 91)
- - `python main.py --cfg config/iu_resnet.yml --expe_name 2nd_try --label_loss --rank_loss --version 12`
- проверить результаты в results
- - свой результат я опубликовал по [ссылке](https://drive.google.com/file/d/12HFamaJtq5Sy4mZyhDNBybIs_9OpWytm/view?usp=sharing) 

## Расположение ключевых файлов
- используемая модель находится по пути ./models/lamrg.py, строчка 421 - LAMRGModel_v12
- трансформер энкодер-декодер опеределен в файле ./modules/Transformer.py, строчка 251 - TransformerModel
- датасет тут - ./modules/datasets.py, строчка 28 - IuxrayMultiImageDataset
- даталоадер тут - ./modules/dataloaders.py, строчка 8 - LADataLoader
- трейнер тут - ./modules/trainer.py, строчка 266 - Trainer

## Описание
- я пыталься проверить версию, согласно которой алгоритму подается одна и та же картинка, но продебажив, увидел что картинки подаются разные 
- я пытался проверить версию что маски у репортов на обучающей выборке всегда нулевые и поэтому модель не видит правильные репорты, однако это оказалось не так...
- пока не разобрался в чем проблема, но могу заметить что метрики даже у такого решения прямо как в статье... наводит на неприятные мысли...



---------------------------


# Radiology Report Generation with a Learned Knowledge Base and Multi-modal Alignment

基于自学习知识库和多模态对其机制的医学报告生成

## Requirements
- `Python >= 3.6`
- `Pytorch >= 1.7`
- `torchvison`
- [Microsoft COCO Caption Evaluation Tools](https://github.com/tylin/coco-caption)
- [CheXpert](https://github.com/stanfordmlgroup/chexpert-labeler)

`conda activate tencent`

## Data

Download IU and MIMIC-CXR datasets, and place them in `data` folder.

- IU dataset from [here](https://iuhealth.org/find-medical-services/x-rays)
- MIMIC-CXR dataset from [here](https://physionet.org/content/mimic-cxr-jpg/2.0.0/)
    
    
## Folder Structure
- config : setup training arguments and data path
- data : store IU and MIMIC dataset
- models: basic model and all our models
- modules: 
    - the layer define of our model 
    - dataloader
    - loss function
    - metrics
    - tokenizer
    - some utils
- pycocoevalcap: Microsoft COCO Caption Evaluation Tools

## Training and Testing
- The validation and testing will run after training.
- More options can be found in `config/opts.py` file.
- The model will be trained using command：
    - $dataset_name:
        - iu: IU dataset
        - mimic: MIMIC dataset
    1. full model
    
        ```
        python main.py --cfg config/{$dataset_name}_resnet.yml --expe_name {$experiment name} --label_loss --rank_loss --version 12
        # python main.py --cfg config/iu_resnet.yml --expe_name 2nd_try --label_loss --rank_loss --version 12 
        # python main.py --cfg config/mimic_resnet.yml --expe_name 1st_mimic_try --label_loss --rank_loss --version 12 
        ```
        
    2. basic model
    
        ```
        python main_basic.py --cfg config/{$dataset_name}_resnet.yml --expe_name {$experiment name} --label_loss --rank_loss --version 91
        ```
        
    3. our model without the learned knowledge base
    
        ```
        python main.py --cfg config/{$dataset_name}_resnet.yml --expe_name {$experiment name} --label_loss --rank_loss --version 92
        ```
        
    4. for the model without multi-modal alignment
        You remove `--label_loss` or `--rank_loss` from the commonds.

## Citation
Shuxin Yang, Xian Wu, Shen Ge, ZhuoZhao Zheng, S. Kevin Zhou, Li Xiao,Radiology Report Generation with a Learned Knowledge Base and Multi-modal Alignment. Medical Image Analysis,2023

## Contact
If you have any problem with the code, please contact Shuxin Yang(aspenstarss@gmail.com) or Li Xiao(andrew.lxiao@gmail.com).
