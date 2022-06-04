import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ProductDetailsComponent } from '@products/product-details/product-details.component';
import { ProductsListComponent } from '@products/products-list/products-list.component';
import { CategoryComponent } from './category/category.component';


const myComponents = [ProductDetailsComponent, ProductsListComponent, CategoryComponent];

@NgModule({
  declarations: [...myComponents],
  imports: [
    CommonModule, RouterModule
  ],
  exports: [...myComponents]
})
export class ProductsModule { }
