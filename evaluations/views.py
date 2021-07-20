# Django
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Models
from .models import Evaluation, Rubro

# Forms
from evaluations.forms import FormEvaluation, FormRubro, \
    FormEvaluationCreate, FormEvaluationUpdate, FormRubroCreate, FormRubroDelete


class Evaluations(ListView):
    """list all evaluations on a template"""
    template_name = "evaluations/evaluations.html"
    context_object_name = 'evaluations'

    def get_queryset(self):
        return Evaluation.objects.all()


@login_required
def list_evaluation(request):
    evaluations_list = Evaluation.objects.all()
    form_evaluation = FormEvaluation()
    rubro_form = FormRubro()
    rubro_delete_form = FormRubroDelete()

    return render(request, template_name='evaluations.html',
                  context={
                      'evaluations_list': evaluations_list,
                      'form': form_evaluation,
                      'rubro_form': rubro_form,
                      'rubro_delete_form': rubro_delete_form,
                  })


@login_required
def create_evaluation(request):
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


@login_required
def delete_evaluation(request):
    if request.method == 'POST':
        evaluation_id = request.POST.get('deleteb')
        evaluation = Evaluation.objects.get(pk=evaluation_id)
        evaluation.delete()

    return redirect('evaluations')


@login_required
def update_evaluation(request, pk):
    evaluation = Evaluation.objects.get(pk=pk)
    evaluation_form = FormEvaluationUpdate(request.POST or None, instance=evaluation)

    context = {
        'update_form': evaluation_form,
        'evaluation': evaluation,
    }

    if request.method == 'POST':

        if evaluation_form.is_valid():

            data_form = evaluation_form.cleaned_data
            evaluation_id = pk
            rubro = data_form['rubro']
            score = data_form['score']
            student = request.POST.get('student')

            Evaluation.objects.filter(pk=evaluation_id).update(
                rubro_id=rubro,
                score=score,
                student_id=student
            )

            return redirect('evaluations')

        else:
            return render(request, template_name='update_evaluation.html', context=context)

    else:
        return render(request, template_name='update_evaluation.html', context=context)


@login_required
def create_rubro(request):
    if request.method == 'POST':

        evaluations_list = Evaluation.objects.all()
        rubro_form = FormRubro(request.POST)

        if rubro_form.is_valid():
            data_form = rubro_form.cleaned_data
            name = data_form['name']
            rubro = Rubro(name=name)
            rubro.save()

            return redirect('evaluations')

        else:
            return render(request, template_name='evaluations.html',
                          context={
                              'rubro_form': rubro_form,
                              'evaluations_list': evaluations_list
                          })

    else:
        rubro_form = FormRubro()
        return render(request, template_name='evaluations.html', context={'rubro_form': rubro_form})


@login_required
def delete_rubro(request):
    evaluations_list = Evaluation.objects.all()

    if request.method == 'POST':

        rubro_form = FormRubroDelete(request.POST)

        if rubro_form.is_valid():
            rubro_id = request.POST.get('name')
            rubro = Rubro.objects.get(pk=rubro_id)
            rubro.delete()

            return redirect('evaluations')

        else:
            return render(request, template_name='evaluations.html',
                          context={
                              'rubro_from': rubro_form,
                              'evaluations_list': evaluations_list

                          })

    return redirect('evaluations')
