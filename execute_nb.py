import nbformat as nbf
import sys
import io
import contextlib
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64

notebook_file = 'Rasika_ECommerce_Sales_BI_Analytics.ipynb'
with open(notebook_file, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Environment setup
global_env = {}

for cell in nb.cells:
    if cell.cell_type == 'code':
        print(f"Executing code cell...")
        code = cell.source
        
        # Capture stdout
        f_out = io.StringIO()
        plt.close('all')
        
        try:
            with contextlib.redirect_stdout(f_out):
                exec(code, global_env)
            
            stdout_str = f_out.getvalue()
            outputs = []
            
            if stdout_str:
                outputs.append(nbf.v4.new_output(output_type='stream', name='stdout', text=stdout_str))
            
            # Capture any matplotlib figure
            figs = [plt.figure(i) for i in plt.get_fignums()]
            for fig in figs:
                buf = io.BytesIO()
                fig.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                img_b64 = base64.b64encode(buf.read()).decode('utf-8')
                outputs.append(nbf.v4.new_output(
                    output_type='display_data',
                    data={'image/png': img_b64, 'text/plain': '<Figure size ...>'}
                ))
            plt.close('all')
            cell.outputs = outputs
        except Exception as e:
            print(f"Error executing cell: {e}")
            cell.outputs = [nbf.v4.new_output(output_type='stream', name='stderr', text=str(e))]

with open(notebook_file, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Notebook {notebook_file} executed and saved with all cell outputs!")
