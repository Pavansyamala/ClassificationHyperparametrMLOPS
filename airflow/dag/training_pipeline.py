from __future__ import annotations
import json
from textwrap import dedent
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.pipeline.training_pipeline import TrainingPipeline

training_pipeline = TrainingPipeline()

with DAG(
    "house_price_prediction",  # Updated DAG name (no spaces)
    description = 'It is my training pipeline',
    schedule='@weekly',  # Corrected schedule argument
    start_date=pendulum.datetime(2024, 10, 18, tz='UTC'),
    catchup=False,  
    tags = ['machine_learning','regression','training','airflow']
) as dag :
    dag.doc_md = __doc__

    def data_ingestion(**kwargs):
        ti = kwargs["ti"]
        training_path, testing_path = training_pipeline.start_data_ingestion()
        ti.xcom_push("data_ingestion_artifacts", {"training_path": training_path, "testing_path": testing_path})

    def data_transformation(**kwargs):
        ti = kwargs['ti']
        data_ingestion_artifact = ti.xcom_pull(task_ids='data_ingestion', key='data_ingestion_artifacts')
        x, y, xt, yt = training_pipeline.start_data_transformation(
            data_ingestion_artifact['training_path'], 
            data_ingestion_artifact['testing_path']
        )
        x = x.tolist()
        y = y.tolist()
        xt = xt.tolist()
        yt = yt.tolist()
        ti.xcom_push("data_transformation_artifact", {"x": x, "y": y, "xt": xt, "yt": yt})

    def model_trainer(**kwargs):
        import numpy as np
        ti = kwargs['ti']
        data_transformation_artifact = ti.xcom_pull(task_ids='data_transformation', key='data_transformation_artifact')
        model_path = training_pipeline.start_model_training(
            np.array(data_transformation_artifact['x']), 
            np.array(data_transformation_artifact['y']), 
            np.array(data_transformation_artifact['xt']), 
            np.array(data_transformation_artifact['yt']),
        )

    data_ingestion_task = PythonOperator(
        task_id='data_ingestion',
        python_callable=data_ingestion
    )
    data_ingestion_task.doc_md = dedent(
        """\
        ### Ingestion Task 
        This task creates train and test files.
        """
    )

    data_transformation_task = PythonOperator(
        task_id='data_transformation',
        python_callable=data_transformation
    )
    data_transformation_task.doc_md = dedent('''\
        ### Data Transformation
        This task creates training and testing arrays after transformations.
        '''
    )

    model_trainer_task = PythonOperator(
        task_id='model_trainer',
        python_callable=model_trainer
    )
    model_trainer_task.doc_md = dedent("""\
        ### Model Training
        This task creates a model.
        """
    )

    data_ingestion_task >> data_transformation_task >> model_trainer_task
