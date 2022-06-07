import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NewCategoryRoutingModule } from './new-category-routing.module';
import { NewCategoryComponent } from './new-category.component';


@NgModule({
  declarations: [
  ],
  imports: [
    CommonModule,
    NewCategoryRoutingModule,
  ]
})
export class NewCategoryModule { }
