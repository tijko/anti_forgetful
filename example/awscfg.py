key_pair_name = 'tutorial_key_pair'
group_name = 'tutorial_group'
volume_name = 'abc'
instance_type = 't2.micro'
no_strict_host_checking = True

#create_ami options
base_image_id = 'ami-428aa838'
root_volume_size = 30 # In GB
image_name = 'myimage'

def setup_images(s):
    s.copy_to_remote('docker-compose.yml')
    s.run_cmd('docker-compose pull')
