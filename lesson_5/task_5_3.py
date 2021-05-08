tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def tutors_by_classes(_tutors, _classes):
    _classes = _classes[::-1]
    for tutor in _tutors:
        if len(_classes):
            yield tuple([tutor, _classes.pop()])
        else:
            yield tuple([tutor, None])


tutors_classes = tutors_by_classes(tutors, classes)

# Show generated tuples from given lists
print(*tutors_classes)

# Show that tutors_classes has <class 'generator'>
print(type(tutors_classes))

# Get all generated elements + 1, to get StopIteration message
tutors_classes = tutors_by_classes(tutors, classes)
for tutor_index in range(len(tutors) + 1):
    print(next(tutors_classes))
