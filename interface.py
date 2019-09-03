import click
from task import shiftEncrypt
from task import matrixEncrypt
from task import shiftDecrypt
from task import matrixDecrypt

@click.command()
@click.argument('text', nargs=-1)
@click.option('--algorithm', type=str, prompt='Name of algorithm (Shift or Matrix)', required=True)
@click.option('--method', type=str, prompt='Encrypt or decrypt', required=True)

def message(text, algorithm, method):
	text_string = ' '.join(text)
	cyphertext = ""

	if algorithm in ['shift', 'Shift', 'SHIFT', 's', 'S']:
		if method in ['encrypt', 'Encrypt', 'ENCRYPT','e', 'E']:
			cyphertext = shiftEncrypt(text_string)
		else:
			cyphertext = shiftDecrypt(text_string)
	else:
		if method in ['encrypt', 'Encrypt', 'ENCRYPT','e', 'E']:
			cyphertext = matrixEncrypt(text_string)
		else:
			cyphertext = matrixDecrypt(text_string)

	click.echo(cyphertext)

if __name__ == '__main__':
    message()