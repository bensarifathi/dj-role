class Teacher(AbstractUserRole):
    available_permissions = {
        
        can_read_student: True,
        
        can_write_student: True,
        
    }