import datetime
long_lorem_ipsum = 'L4-5: degenerative annular disc bulge is noted more to the left side compressing thecal sac, compressing left nerve root and narrowing right neural foramen. // Evidence of hyperintense signal within the annulus fibrosus at left paramedian/posterolateral area which probably represents a torn annulus.'
sample_data = {}
patient_data = {}
patient_data_rank = {}
short_lorem_ipsum = 'Patient declares he is feeling tired all day, strong lower back pain'
skills = "Skills"
hobbies = "Hobbies"

# This class holds sample data used by some generated pages to show how they can be used.
# TODO Web Template Studio: Delete this file once your app is using real data.
patient_data['text_assets'] = [
    {
        'shortDescription': "5. " + short_lorem_ipsum,
        'longDescription': "LSS MRI:Feature of muscle spasm. Diffuse disc bulge noted ar L4/L5 level, mildly compressing the thecal sac and both exit nerve roots",
        'name': 'Patient A',
        'status': 'None',
        'shipFrom': 'Francisco Perez-Olaeta',
        'age': 24.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 1
    },
    {
        'shortDescription': "2. " + short_lorem_ipsum,
        'longDescription': "No evidence of disc herniation. No significant thecal sac or nerve root compression noted.",
        'name': 'Patient B',
        'status': 'None',
        'shipFrom': 'Soo Jung Lee',
        'age': 60.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 2
    },
    {
        'shortDescription': "3. " + short_lorem_ipsum,
        'longDescription': "LSS MRI Features of muscle spasm. small central  disc protrusion noted at L5-S1 level abutting the thecal sac. no significant thecal  sac or nerve root compression noted. ",
        'name': 'Patient C',
        'status': 'None',
        'shipFrom': 'Run Liu',
        'age': 65.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 3
    },
    {
        'shortDescription': "6. " + short_lorem_ipsum,
        'longDescription': "LSS MRI: Feature of muscle spasm. Diffuse disc bulge noted at L4/L5 level, mild compressing thecal sac and both nerve roots . Wide base disc bulges noted at L5/S1 level, mild compressing thecal sac and both nerve roots ",
        'name': "Patient D",
        'status': "None",
        'shipFrom': "Soo Jung Lee",
        'age': 56.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 4
    },
    {
        'shortDescription': "10. " + short_lorem_ipsum,
        'longDescription': "LSS MRI. no evidence of disc herniation. no significant thecal sac or nerve root compression noted. ",
        'name': "Patient E",
        'status': "None",
        'shipFrom': "John Rodman",
        'age': 81.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 5
    },
    {
        'shortDescription': "12. " + short_lorem_ipsum,
        'longDescription': "LSS MRI. Rt paracentral disc protrusion noted at L4-L5 level, compressing the thecal sac. Adequate spinal canal. ",
        'name': "Patient F",
        'status': "None",
        'shipFrom': "Elizabeth Andersen",
        'age': 56.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 6
    },
    {
        'shortDescription': "13. " + short_lorem_ipsum,
        'longDescription': "L4-5 broad based central and left paracentral disc protrusion is noted compressing thecal sac and narrowing left neural foramen./// L5-S1: broad based degenerative central disc bulge is noted indenting thecal sac but not causing significant nerve root compression or foraminal narrowing.//// dehydrated L4-5 and L5-S1 intervetrebral discs./// vertebral bone marrow signal reconversion is noted.",
        'name': "Patient G",
        'status': "None",
        'shipFrom': "Peter Krschne",
        'age': 27.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 7
    },
    {
        'shortDescription': "16. " + short_lorem_ipsum,
        'longDescription': "Lumbosacral MRI. Features of muscle spasm. Dissicating   lower disc space noted. - Central and left paracentral disc protrusion noted at L4-L5 level compressing the thecal sac and Lt exit nerve root. - Diffuse Disc bulges noted at the L5-S1 level, mild compressing the thecal sac and exiting nerve root.",
        'name': "Patient H",
        'status': "None",
        'shipFrom': "Sven Mortensen",
        'age': 73.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 8
    },
    {
        'shortDescription': "17. " + short_lorem_ipsum,
        'longDescription': "L5-S1: left paramedian disc protrusion on top of degenerative annular disc bulge causing compression of thecal sac, compressing left S1 nerve root within lateral recess, compressing left L5 nerve root within left neural foramen and narrowing right neural foramen./// L4-5: annular disc bulge is noted compressing thecal sac and narrowing both neural foramina/// L3-4: left posterolateral disc bulge is notedslightly narrowing left neural foramen.",
        'name': "Patient I",
        'status': "None",
        'shipFrom': "Anna Bedecs",
        'age': 80.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 9
    }
]
# Patient 10 is the patient 23 in the excel file

patient_data_rank['text_assets'] = [
    {
        'shortDescription': "5. " + short_lorem_ipsum,
        'longDescription': "LSS MRI:Feature of muscle spasm. Diffuse disc bulge noted ar L4/L5 level, mildly compressing the thecal sac and both exit nerve roots",
        'name': 'Patient A',
        'status': 'Protrusion',
        'shipFrom': 'Francisco Perez-Olaeta',
        'age': 24.0,
        'probability': 0.7,
        'orderDate': datetime.datetime.now(),
        'id': 1
    },
    {
        'shortDescription': "2. " + short_lorem_ipsum,
        'longDescription': "No evidence of disc herniation. No significant thecal sac or nerve root compression noted.",
        'name': 'Patient B',
        'status': 'Normal',
        'shipFrom': 'Soo Jung Lee',
        'age': 60.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 2
    },
    {
        'shortDescription': "3. " + short_lorem_ipsum,
        'longDescription': "LSS MRI Features of muscle spasm. small central  disc protrusion noted at L5-S1 level abutting the thecal sac. no significant thecal  sac or nerve root compression noted. ",
        'name': 'Patient C',
        'status': 'Protrusion',
        'shipFrom': 'Run Liu',
        'age': 65.0,
        'probability': 0.6,
        'orderDate': datetime.datetime.now(),
        'id': 3
    },
    {
        'shortDescription': "6. " + short_lorem_ipsum,
        'longDescription': "LSS MRI: Feature of muscle spasm. Diffuse disc bulge noted at L4/L5 level, mild compressing thecal sac and both nerve roots . Wide base disc bulges noted at L5/S1 level, mild compressing thecal sac and both nerve roots ",
        'name': "Patient D",
        'status': "Protrusion",
        'shipFrom': "Soo Jung Lee",
        'age': 56.0,
        'probability': 0.8,
        'orderDate': datetime.datetime.now(),
        'id': 4
    },
    {
        'shortDescription': "10. " + short_lorem_ipsum,
        'longDescription': "LSS MRI. no evidence of disc herniation. no significant thecal sac or nerve root compression noted. ",
        'name': "Patient E",
        'status': "Normal",
        'shipFrom': "John Rodman",
        'age': 81.0,
        'probability': 0,
        'orderDate': datetime.datetime.now(),
        'id': 5
    },
    {
        'shortDescription': "12. " + short_lorem_ipsum,
        'longDescription': "LSS MRI. Rt paracentral disc protrusion noted at L4-L5 level, compressing the thecal sac. Adequate spinal canal. ",
        'name': "Patient F",
        'status': "Protrusion",
        'shipFrom': "Elizabeth Andersen",
        'age': 56.0,
        'probability': 0.9,
        'orderDate': datetime.datetime.now(),
        'id': 6
    },
    {
        'shortDescription': "13. " + short_lorem_ipsum,
        'longDescription': "L4-5 broad based central and left paracentral disc protrusion is noted compressing thecal sac and narrowing left neural foramen./// L5-S1: broad based degenerative central disc bulge is noted indenting thecal sac but not causing significant nerve root compression or foraminal narrowing.//// dehydrated L4-5 and L5-S1 intervetrebral discs./// vertebral bone marrow signal reconversion is noted.",
        'name': "Patient G",
        'status': "Protrusion",
        'shipFrom': "Peter Krschne",
        'age': 27.0,
        'probability': 0.4,
        'orderDate': datetime.datetime.now(),
        'id': 7
    },
    {
        'shortDescription': "16. " + short_lorem_ipsum,
        'longDescription': "Lumbosacral MRI. Features of muscle spasm. Dissicating   lower disc space noted. - Central and left paracentral disc protrusion noted at L4-L5 level compressing the thecal sac and Lt exit nerve root. - Diffuse Disc bulges noted at the L5-S1 level, mild compressing the thecal sac and exiting nerve root.",
        'name': "Patient H",
        'status': "Protrusion",
        'shipFrom': "Sven Mortensen",
        'age': 73.0,
        'probability': 0.7,
        'orderDate': datetime.datetime.now(),
        'id': 8
    },
    {
        'shortDescription': "17. " + short_lorem_ipsum,
        'longDescription': "L5-S1: left paramedian disc protrusion on top of degenerative annular disc bulge causing compression of thecal sac, compressing left S1 nerve root within lateral recess, compressing left L5 nerve root within left neural foramen and narrowing right neural foramen./// L4-5: annular disc bulge is noted compressing thecal sac and narrowing both neural foramina/// L3-4: left posterolateral disc bulge is notedslightly narrowing left neural foramen.",
        'name': "Patient I",
        'status': "Protrusion",
        'shipFrom': "Anna Bedecs",
        'age': 80.0,
        'probability': 0.8,
        'orderDate': datetime.datetime.now(),
        'id': 9
    }
]


sample_data['member_assets'] = [
    {
        'shortDescription': hobbies,
        'longDescription': skills,
        'title': 'Edwin Duque',
        'status': 'None',
        'shipTo': 'Systems Engineering',
        'orderTotal': 36.0,
        'orderDate': datetime.datetime.now(),
        'id': 1
    },
    {
        'shortDescription': hobbies,
        'longDescription': skills,
        'title': 'Sebastian Zambrano',
        'status': 'None',
        'shipTo': 'Business Administrator',
        'orderTotal': 30.0,
        'orderDate': datetime.datetime.now(),
        'id': 2
    },
    {
        'shortDescription': hobbies,
        'longDescription': skills,
        'title': 'Sebastian Florez',
        'status': 'None',
        'shipTo': 'Systems Engineering',
        'orderTotal': 28.0,
        'orderDate': datetime.datetime.now(),
        'id': 3
    },
    {
        'shortDescription': hobbies,
        'longDescription': skills,
        'title': "Ruben Yepes",
        'status': "None",
        'shipTo': "Statistician",
        'orderTotal': 29.0,
        'orderDate': datetime.datetime.now(),
        'id': 4
    }
]
