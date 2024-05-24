from django.shortcuts import render
from django.core.cache import cache
from . import files
## from django.core.cache import cache

def index(request):
    return render(request, "index.html", context={})

def problems(request):
    problems = files.get_problems_for_table()
    sections_dict = files.get_sections_dict()
    return render(request, "problems.html", context={"problems":problems, "sections_dict":sections_dict})

def refs(request):
    print(request.method)
    if not(request.method == "POST"):
        references = files.get_references()
        print(references)
        return render(request, "references.html", context={"references":references})
    
    cache.clear()
    author = str(request.POST.get("author"))
    title = str(request.POST.get("title"))
    link = str(request.POST.get("link"))

    files.add_ref(author, title, link)
    references = files.get_references()
    return render(request, "references.html", context={"references":references})

def add_form(request):
    cache.clear()
    sections_list = files.get_sections()
    context={"sections_list": sections_list}
    context["problem_posted"] = (request.method == "POST")
    if not context["problem_posted"]:
        return render(request, "form.html", context=context)
    section = request.POST.get("section")

    if section == None:
        context["success"] = False
        context["comment"] = "Вы не выбрали раздел."
        return render(request, "form.html", context=context)
    
    problem_text = request.POST.get("problem_text")
    if len(problem_text)==0:
        context["success"] = False
        context["comment"] = "Вы не написали текст задачи." 
        return render(request, "form.html", context=context)

    if int(section) == 0:
        new_section = request.POST.get("new_section")
        if len(new_section)==0:
            context["success"] = False
            context["comment"] = "Вы не написали раздел."
            return render(request, "form.html", context=context)
        else:
            files.add_section(new_section)
            context["sections_list"] = files.get_sections()
    section_num = int(section) if (int(section) != 0) else len(files.get_sections_dict())
    files.write_problem(section_num, problem_text)
    print(problem_text)
    context["success"] = True
    context["comment"] = "Задача успешно добавлена."
    return render(request, "form.html", context)