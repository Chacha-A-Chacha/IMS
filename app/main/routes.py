#!usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, flash
from app import db  # Import db from the main __init__.py file
from ..models import User, Category, Item
from . import main


@main.route('/dashboard', methods=['GET'])
def dashboard():
    categories = Category.query.all()
    return render_template('dashboard.html', inventory_categories=categories)

@main.route('/', methods=['GET'])
def inventory():
    categories = Category.query.all()
    return render_template('inv.html', inventory_categories=categories)


@main.route('/update_inventory', methods=['POST'])
def update_inventory():
    if request.method == 'POST':
        category_id = request.form['category_id']
        for item in Category.query.get(category_id).items:
            quantity_taken = request.form.get(f'quantity_taken_{item.id}')
            quantity_returned = request.form.get(f'quantity_returned_{item.id}')

            if quantity_taken:
                item.quantity -= int(quantity_taken)
            if quantity_returned:
                item.quantity += int(quantity_returned)

            db.session.commit()

        flash('Inventory updated successfully!', 'success')
        return redirect(url_for('inventory'))
