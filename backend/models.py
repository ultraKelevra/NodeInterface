from flask import render_template, jsonify
import pandas as pd
from forms import *

class FormElement:
    def __init__(self, label, type):
        self.label = label
        self.tag = tag

class NodeBlueprint:
    def __init__(self):
        self.ready=false
        self.outputs=[]
        self.inputs=[]
        self.form=[]

    def getJson(self):
        dict={
        "inputs":self.inputs
        "outputs":self.outputs
        "form":self.form
        }
class Node:
    def __init__(self,blueprint):
        self.blueprint=blueprint
        self.outputs=[]
        self.inputs=[]
        self.form=[]
        for input in blueprint.inputs:
            self.inputs.append(generate_input(input))
        for output in blueprint.outputs:
            self.outputs.append(generate_output(output))
        for form in blueprint.form:
            self.form.append(generate_form(form))