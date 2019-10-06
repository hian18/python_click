import click
import os
import shutil
# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)

@click.command()
@click.option('--recurso', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(recurso, name:str):
    file_name='resource_'+name+'.py'

    with open(file_name,'w') as file:
        
        
        recurso='from marshmallow_sqlalchemy import ModelSchema\n'\
                'from marshmallow_sqlalchemy.fields import fields\n'\
                '\n'\
                'class {}Schema(ModelSchema):\n'\
                '    pass\n'\
                '{}_schema={}Schema()\n'
        recurso=recurso.format(name.title(),name.lower(),name.title())
        breakpoint()
        file.write(recurso)
        file.close()
        shutil.move(f'./{file_name}','./schema')



if __name__ == '__main__':
    hello()