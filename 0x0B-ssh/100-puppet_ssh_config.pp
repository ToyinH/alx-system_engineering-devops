# configure configuration file using puppet

$file_path = '/etc/ssh/ssh_config'

file { $file_path:
  ensure  => 'present',
  content => "
	# SSH client configuration
	host*
	PasswordAuthentication no
	IdentityFile ~/.ssh/school
	"
}
