from django.shortcuts import render, redirect, HttpResponse
from evaluations.models import Evaluation, Rubro
from evaluations.forms import FormEvaluation, FormRubro,FormEvaluationCreate
# Create your views here.


def list_evaluation(request):
    evaluations_list = Evaluation.objects.all()
    form_evaluation = FormEvaluation()

    return render(request, template_name='evaluations.html',
                  context={
                      'evaluations_list': evaluations_list,
                      'form': form_evaluation
                  })


def create_evaluation(request):
    print(request.POST)
    if request.method == 'POST':

        evaluation_form = FormEvaluationCreate(request.POST)

        if evaluation_form.is_valid():
            data_form = evaluation_form.cleaned_data
            rubro = request.POST['rubro']
            score = data_form['score']
            student = request.POST['student']

            evaluation = Evaluation(
                rubro_id=rubro,
                score=score,
                student_id=student
            )
            evaluation.save()

            return redirect('evaluations')

        else:
            evaluations_list = Evaluation.objects.all()

            return render(request, template_name='evaluations.html',
                          context={
                              'form': evaluation_form,
                              'evaluations_list': evaluations_list
                          })

    else:
        return HttpResponse('Error: This method is not allowed')




def delete_evaluation(request):
    pass


def update_evaluation(request):
    pass
