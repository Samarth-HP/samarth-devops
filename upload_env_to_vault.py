# Python script to transfer key=value pairs from local env file to vault while onboarding 

import sys, os

for i in sys.argv:
    print(i)
    
env_file = sys.argv[1]
vault_path = sys.argv[2]


# If vault path does not exists make a one
# This rewrites all the key-value pairs for a vault path 
os.system(f'vault kv put -mount=kv {vault_path} TEST_ENV=TEST_ENV')

with open(env_file, 'r') as f:  
    lines = f.readlines()
    for l in lines:
        try:
            key, value = l.split('=')
        except ValueError:
            print(l)
        else:
            command = f'vault kv patch -mount=kv {vault_path} {key}={value}'
            os.system(command)
            

print()
print("# FOR ENV TEMPLATES")

with open(env_file, 'r') as f:  
    lines = f.readlines()
    for l in lines:
        try:
            key, value = l.split('=')
        except ValueError:
            print(l)
        else:
            print(f'{key}={{{{ credentials.{key} }}}}')
            
print()
print("# FOR VARS/MAIN")
            
with open(env_file, 'r') as f:  
    lines = f.readlines()
    for l in lines:
        try:
            key, value = l.split('=')
        except ValueError:
            print(l)
        else:
            print(f'{key}:"{{{{ credentials.{key} }}}}"')
            