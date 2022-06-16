import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrderControlComponent } from './order-control.component';

const routes: Routes = [{ path: '', component: OrderControlComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class OrderControlRoutingModule { }
