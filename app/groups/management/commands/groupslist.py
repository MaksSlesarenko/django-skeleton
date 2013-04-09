from django.core.management.base import NoArgsCommand
from django.db.models import Count

from optparse import make_option

from app.groups.models import Group
from app.students.models import Student



class Command( NoArgsCommand ):
    option_list = NoArgsCommand.option_list + (
        make_option('--with-students', action='store_true', dest='students', default= False,
            help='Add students information' ),
    )
    help = 'Prints model names for given application and optional object count.'

    def handle_noargs(self, **options):
        
        groups = Group.objects.annotate(num_students=Count('user_to_group'))

        lines = []
        lines.append( "Groups:" )
        
        for group in groups:
            lines.append( "%s" % group.name + " (%d)" % group.num_students )
            
            if (options['students']):
                students = Student.objects.filter(group = group)
                
                lines.append( "\t Students:" )
                for student in students:
                    lines.append( "\t %s %s" % (student.first_name, student.last_name) )

        return "\n".join( lines )